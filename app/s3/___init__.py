import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from botocore.exceptions import ClientError

import urllib.parse

class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config, verify=False ) as client:
            yield client

    async def upload_file(
            self,
            file_path: str,
    ):
        object_name = '1/' + file_path.split("/")[-1]  # /users/artem/cat.jpg
        try:
            async with self.get_client() as client:
                with open(file_path, "rb") as file:
                    await client.put_object(
                        Bucket=self.bucket_name,
                        Key=object_name,
                        Body=file,
                    )
                print(f"File {object_name} uploaded to {self.bucket_name}")
        except ClientError as e:
            print(f"Error uploading file: {e}")

    async def delete_file(self, object_name: str):
        try:
            async with self.get_client() as client:
                await client.delete_object(Bucket=self.bucket_name, Key=object_name)
                print(f"File {object_name} deleted from {self.bucket_name}")
        except ClientError as e:
            print(f"Error deleting file: {e}")
            
    async def list_files(self, prefix: str):
        try:
            async with self.get_client() as client:
                paginator = client.get_paginator('list_objects_v2')
                result = []
                async for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
                    for obj in page.get('Contents', []):
                        key = obj['Key']
                        url = f"{self.config['endpoint_url']}/{key}"
                        result.append(url)
                return result
        except ClientError as e:
            print(f"Error listing files: {e}")
            return []


async def main():
    s3_client = S3Client(
        access_key="1f82675d0dda4a6cb064b69ff4e20c18",
        secret_key="7a5ffb58e8af44d5b33fbc0745d00a7f",
        endpoint_url="https://file.s3.ussrwatch.ru",
        bucket_name="watch",
    )

# https://file.s3.ussrwatch.ru/watch/bottom.jpg
# https://file.s3.ussrwatch.ru/watch/left.jpg
# https://file.s3.ussrwatch.ru/1/left.jpg
# https://file.s3.ussrwatch.ru/watch/right.jpeg
# https://file.s3.ussrwatch.ru/watch/top.jpg

    await s3_client.upload_file("bottom.jpg")
    await s3_client.upload_file("left.jpg")
    await s3_client.upload_file("right.jpeg")
    await s3_client.upload_file("top.jpg")
    
    files = await s3_client.list_files('1/')
    for file_url in files:
        print(file_url)
    
if __name__ == "__main__":
    asyncio.run(main())