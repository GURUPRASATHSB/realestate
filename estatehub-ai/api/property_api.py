from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.property_database import init_db,SessionLocal
from app.client_memory import get_or_create_client,save_search
from app.property_planner import plan_property_search
from schema.real_estate_models import PropertyRequest,FinalPropertyPlan
init_db()
app=FastAPI(title="EstateHub AI",version="1.0.0")
def db_session():
    db=SessionLocal()
    try: yield db
    finally: db.close()
@app.get("/health")
def health(): return {"status":"ok","mode":"mock/demo"}
@app.post("/properties/plan",response_model=FinalPropertyPlan)
def plan(request:PropertyRequest,db:Session=Depends(db_session)):
    c=get_or_create_client(db,request.client_name); request.client_id=c.id
    save_search(db,c.id,request.location)
    return plan_property_search(request)
