from app.real_estate_providers import MockRealEstateProvider
provider=MockRealEstateProvider()
def get_area_insights(location):
    return provider.area_insights(location)
