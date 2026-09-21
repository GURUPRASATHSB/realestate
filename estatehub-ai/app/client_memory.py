from sqlalchemy.orm import Session
from app.property_database import Client,SearchHistory
def get_or_create_client(db:Session,name:str,contact:str=""):
    c=db.query(Client).filter(Client.name==name).first()
    if not c:
        c=Client(name=name,contact=contact); db.add(c); db.commit(); db.refresh(c)
    return c
def save_search(db:Session,client_id:int|None,query:str):
    db.add(SearchHistory(client_id=client_id,query=query)); db.commit()
