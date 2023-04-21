from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base


"""DB Connection"""
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

db_connection = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(db_connection)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine, checkfirst=True)
