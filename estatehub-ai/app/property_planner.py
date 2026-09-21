from app.real_estate_agents import build_graph
from schema.real_estate_models import FinalPropertyPlan
def plan_property_search(request):
    result=build_graph().invoke({"request":request})
    return FinalPropertyPlan(request=request,properties=result["properties"],area_insights=result["area_insights"],property_visit=result["property_visit"],affordability=result["affordability"],validation=result["validation"],disclaimer="Demo/mock real-estate data only. Verify listing availability, ownership, title, approvals, pricing, taxes, loan terms and legal documents with qualified professionals before making a transaction.")
