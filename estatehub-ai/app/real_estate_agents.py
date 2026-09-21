from typing import TypedDict,Any
from langgraph.graph import StateGraph,START,END
from app.real_estate_providers import MockLLMProvider
from app.tools.property_listing_search import search_properties
from app.tools.location_insights import get_area_insights
from app.tools.property_visit_scheduler import find_visit_slots
from app.tools.property_loan_calculator import estimate_affordability
class EstateState(TypedDict,total=False):
    request:Any
    interpretation:dict
    properties:list
    area_insights:list
    property_visit:dict
    affordability:dict
    validation:dict
llm=MockLLMProvider()
def orchestrator(state):
    r=state["request"]
    state["interpretation"]=llm.interpret(" ".join([r.property_type or "",r.purpose or "",r.location]))
    return state
def property_agent(state):
    r=state["request"]
    typ=r.property_type or state["interpretation"]["property_type"]
    rows=search_properties(r.location,typ)
    if r.bedrooms is not None: rows=[x for x in rows if x["bedrooms"]>=r.bedrooms] or rows
    if r.budget is not None: rows=[x for x in rows if x["price"]<=r.budget] or rows
    state["properties"]=rows
    return state
def area_agent(state):
    state["area_insights"]=[get_area_insights(state["request"].location)]
    return state
def visit_agent(state):
    r=state["request"]; p=state["properties"][0]
    state["property_visit"]=find_visit_slots(p["id"],r.location if False else "2026-09-22",None)[0]
    return state
def affordability_agent(state):
    r=state["request"]; p=state["properties"][0]
    state["affordability"]=estimate_affordability(p["price"],r.budget)
    return state
def validation_agent(state):
    r=state["request"]; errors=[]; warnings=[]
    if not state.get("properties"): errors.append("No matching properties found.")
    if r.max_area_sqft and state["properties"][0]["area_sqft"]>r.max_area_sqft: warnings.append("Selected property exceeds the requested maximum area.")
    if r.budget and state["properties"][0]["price"]>r.budget: warnings.append("Selected property exceeds the requested budget.")
    state["validation"]={"valid":not errors,"warnings":warnings,"errors":errors}
    return state
def build_graph():
    g=StateGraph(EstateState)
    for n,f in [("orchestrator",orchestrator),("property",property_agent),("area",area_agent),("visit",visit_agent),("affordability",affordability_agent),("validation",validation_agent)]: g.add_node(n,f)
    g.add_edge(START,"orchestrator"); g.add_edge("orchestrator","property"); g.add_edge("property","area"); g.add_edge("area","visit"); g.add_edge("visit","affordability"); g.add_edge("affordability","validation"); g.add_edge("validation",END)
    return g.compile()
