from typing import List,Optional
from pydantic import BaseModel,Field
class PropertyRequest(BaseModel):
    client_id:Optional[int]=None
    client_name:str=Field(min_length=1)
    location:str=Field(min_length=1)
    property_type:Optional[str]=None
    purpose:Optional[str]=None
    budget:Optional[float]=None
    bedrooms:Optional[int]=Field(default=None,ge=0)
    min_area_sqft:Optional[float]=None
    max_area_sqft:Optional[float]=None
    amenities:List[str]=[]
    furnishing:Optional[str]=None
class PropertyOption(BaseModel):
    id:str
    title:str
    property_type:str
    location:str
    price:float
    bedrooms:int
    area_sqft:float
    furnishing:str
    amenities:List[str]
    distance_km:float
class AreaInsight(BaseModel):
    location:str
    average_price:float
    connectivity:str
    nearby_facilities:List[str]
    note:str
class PropertyVisit(BaseModel):
    property_id:str
    property_title:str
    date:str
    time:str
    available:bool
    status:str
class Affordability(BaseModel):
    property_price:float
    down_payment:float
    estimated_loan_amount:float
    estimated_monthly_emi:float
    within_budget:Optional[bool]=None
class ValidationResult(BaseModel):
    valid:bool
    warnings:List[str]=[]
    errors:List[str]=[]
class FinalPropertyPlan(BaseModel):
    request:PropertyRequest
    properties:List[PropertyOption]
    area_insights:List[AreaInsight]
    property_visit:PropertyVisit
    affordability:Affordability
    validation:ValidationResult
    disclaimer:str
