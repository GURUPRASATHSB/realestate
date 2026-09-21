from app.real_estate_providers import MockRealEstateProvider
provider=MockRealEstateProvider()
def find_visit_slots(property_id,date,time=None):
    return provider.visit_slots(property_id,date,time)
