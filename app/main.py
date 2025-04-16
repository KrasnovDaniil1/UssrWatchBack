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
from crud.create import create_tables
from database.config import engine
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

# routers
from routers.watch import router as watch_routers
from routers.mechanisms import router as mechanisms_routers

app.include_router(watch_routers, prefix="/api", tags=["Watch"])
app.include_router(mechanisms_routers, prefix="/api", tags=["Mechanisms"])




    



