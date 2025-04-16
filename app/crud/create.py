from database.tables import Base
from database.config import engine


def create_tables():
    engine.echo = True
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

