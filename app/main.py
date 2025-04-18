# app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# routers
from app.api import router 

# database
from app.database.config import engine
from app.crud.create import create_db, create_data
        
async def lifespan(app: FastAPI):
    await create_db()
    await create_data()
    yield
    await engine.dispose()

main_app = FastAPI(title="UssrWatch API", lifespan = lifespan)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:8080',
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(router, prefix="/api")

# ! убрать
if __name__ == "__main__":
    uvicorn.run("main.py", reload=False)



    



