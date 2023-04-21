from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Table
# from app import engine
from db.db_connect import Base,engine

class Credentials(Base):
    __tablename__ ='user_credentials'
    id= Column(Integer,primary_key=True,autoincrement=True)
    user_name= Column(String)
    password= Column(String)
    app_name= Column(String)
    web_URL= Column(String)

Base.metadata.create_all(engine, checkfirst=True)