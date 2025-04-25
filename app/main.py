import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router 
from api.errors import register_handlers

from crud import start_db

main_app = FastAPI(title="UssrWatch API", lifespan = start_db)
register_handlers(main_app)

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



    



