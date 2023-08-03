##for SQL RAW
# import psycopg2
# from psycopg2.extras import RealDictCursor

##for using ORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import loginSettings
from fastapi import HTTPException, status


SQLALCHEMY_DATABASE_URL = f"postgresql://{loginSettings.database_username}:{loginSettings.database_password}@{loginSettings.database_hostname}:{loginSettings.database_port}/{loginSettings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# conn = psycopg2.connect(host='localhost', database='GMAIL API', user='postgres', password='Jackalis.SQL', cursor_factory=RealDictCursor)
# cursor = conn.cursor()

print("Database connection was succesfull!")

def connect_to_database():
    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()
