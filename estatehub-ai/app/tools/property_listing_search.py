from app.real_estate_providers import MockRealEstateProvider
provider=MockRealEstateProvider()
def search_properties(location,property_type=None):
    return provider.search_properties(location,property_type)
