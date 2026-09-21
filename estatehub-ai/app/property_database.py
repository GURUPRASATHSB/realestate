from sqlalchemy import create_engine,Column,Integer,String,Text,Float,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime
from app.estatehub_config import DATABASE_URL
connect_args={"check_same_thread":False} if DATABASE_URL.startswith("sqlite") else {}
engine=create_engine(DATABASE_URL,connect_args=connect_args)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
class Client(Base):
    __tablename__="clients"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    contact=Column(String,default="")
class PropertyInquiry(Base):
    __tablename__="property_inquiries"
    id=Column(Integer,primary_key=True)
    client_id=Column(Integer,nullable=False)
    location=Column(String,nullable=False)
    property_type=Column(String,default="")
    budget=Column(Float,nullable=True)
    purpose=Column(String,default="")
    status=Column(String,default="active")
class SearchHistory(Base):
    __tablename__="search_history"
    id=Column(Integer,primary_key=True)
    client_id=Column(Integer,nullable=True)
    query=Column(Text,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
def init_db():
    Base.metadata.create_all(bind=engine)
