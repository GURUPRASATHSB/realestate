from app.real_estate_agents import validation_agent
def test_validation():
    state={"request":type("R",(),{"budget":8000000,"max_area_sqft":2000})(),"properties":[{"price":7000000,"area_sqft":1500}]}
    assert validation_agent(state)["validation"]["valid"]
