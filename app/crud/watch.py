from database import connection

@connection
async def create_brand(username: str, email: str, password: str, session: AsyncSession) -> int:
