# database
from app.crud.create import create_tables
from app.database.config import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)

with Session() as session:
    try:
        create_tables()
    except:
        session.rollback()
        raise
    else:
        session.commit()

# app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

main_app = FastAPI(title="UssrWatch API")

main_app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:8080',
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
from app.api import router 

main_app.include_router(router, prefix="/api")

# ! убрать
if __name__ == "__main__":
    uvicorn.run("main.py", reload=False)


    



