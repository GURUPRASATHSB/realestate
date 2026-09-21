from abc import ABC,abstractmethod
class RealEstateProvider(ABC):
    @abstractmethod
    def search_properties(self,location,property_type=None): ...
    @abstractmethod
    def area_insights(self,location): ...
    @abstractmethod
    def visit_slots(self,property_id,date,time): ...
class MockRealEstateProvider(RealEstateProvider):
    DATA=[
      {"id":"P001","title":"Demo Marina Heights","property_type":"Apartment","location":"Chennai","price":6500000,"bedrooms":2,"area_sqft":1100,"furnishing":"Semi-Furnished","amenities":["Parking","Gym","Security"],"distance_km":3.2},
      {"id":"P002","title":"Demo OMR Residency","property_type":"Apartment","location":"Chennai","price":8500000,"bedrooms":3,"area_sqft":1450,"furnishing":"Fully Furnished","amenities":["Parking","Pool","Gym"],"distance_km":5.1},
      {"id":"P003","title":"Demo Tambaram Villa","property_type":"Villa","location":"Chennai","price":11500000,"bedrooms":3,"area_sqft":1800,"furnishing":"Semi-Furnished","amenities":["Garden","Parking","Security"],"distance_km":7.4},
      {"id":"P004","title":"Demo City Office Space","property_type":"Commercial","location":"Chennai","price":12000000,"bedrooms":0,"area_sqft":2200,"furnishing":"Unfurnished","amenities":["Parking","Power Backup","Lift"],"distance_km":4.6}
    ]
    def search_properties(self,location,property_type=None):
        rows=[x for x in self.DATA if location.lower() in x["location"].lower()]
        if property_type:
            match=[x for x in rows if property_type.lower() in x["property_type"].lower()]
            if match: rows=match
        return rows or self.DATA
    def area_insights(self,location):
        return {"location":location,"average_price":7500000,"connectivity":"Demo connectivity information","nearby_facilities":["Schools","Hospitals","Shopping","Public transport"],"note":"Mock area insight; verify current local data before making a property decision."}
    def visit_slots(self,property_id,date,time):
        times=[time] if time else ["10:00","12:00","15:30","17:30"]
        title=next((x["title"] for x in self.DATA if x["id"]==property_id),property_id)
        return [{"property_id":property_id,"property_title":title,"date":date,"time":t,"available":True,"status":"demo-ready"} for t in times]
class LLMProvider(ABC):
    @abstractmethod
    def interpret(self,text): ...
class MockLLMProvider(LLMProvider):
    def interpret(self,text):
        t=text.lower()
        typ=next((x for x in ["apartment","villa","commercial","plot","house"] if x in t),None)
        purpose="investment" if "invest" in t else ("rent" if "rent" in t else "purchase")
        return {"property_type":typ,"purpose":purpose}
