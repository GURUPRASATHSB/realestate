from schema.real_estate_models import PropertyRequest
from app.property_planner import plan_property_search
def test_plan():
    r=PropertyRequest(client_name="Test",location="Chennai",property_type="Apartment",budget=8000000,bedrooms=2)
    p=plan_property_search(r)
    assert p.validation.valid
    assert p.properties
