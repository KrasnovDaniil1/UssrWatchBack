from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api import router 

# from database import engine
from crud import create_db, create_data

from asyncio import run
# from crud.seed_data import select_all_brand

async def lifespan(app: FastAPI):
    await create_db()
    await create_data()
    # all_users = await select_all_brand()
    # for i in all_users:
    #     print(i.to_dict())
    yield
    # await engine.dispose()


main_app = FastAPI(title="UssrWatch API", lifespan = lifespan)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:8080',
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        reload=True,
    )



    



