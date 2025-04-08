# app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="UssrWatch API")

app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:8080',
    allow_methods=["*"],
    allow_headers=["*"],
)

# database
from app.database import session 

session.createDatabase()

# routers
from app.routers import watch as watch_routers
from app.routers import mechanisms as mechanisms_routers

app.include_router(watch_routers.router, prefix="/api", tags=["Watch"])
app.include_router(mechanisms_routers.router, prefix="/api", tags=["Mechanisms"])




    



