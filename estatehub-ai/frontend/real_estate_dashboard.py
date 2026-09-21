import requests,streamlit as st
st.set_page_config(page_title="EstateHub AI",page_icon="🏠",layout="wide")
st.title("🏠 EstateHub AI")
st.caption("Agentic multi-agent real-estate discovery assistant • DEMO/MOCK mode")
with st.form("property"):
    c1,c2=st.columns(2)
    with c1:
        name=st.text_input("Client Name","Demo Client")
        location=st.text_input("Location","Chennai")
        typ=st.selectbox("Property Type",["Apartment","Villa","Commercial","Plot","House"])
        purpose=st.selectbox("Purpose",["Purchase","Rent","Investment"])
        bedrooms=st.number_input("Minimum Bedrooms",0,10,2)
    with c2:
        budget=st.number_input("Budget (₹)",0.0,100000000.0,8000000.0)
        min_area=st.number_input("Minimum Area (sqft)",0.0,100000.0,0.0)
        max_area=st.number_input("Maximum Area (sqft)",0.0,100000.0,0.0)
        furnishing=st.selectbox("Furnishing",["Any","Unfurnished","Semi-Furnished","Fully Furnished"])
    amenities=st.multiselect("Amenities",["Parking","Gym","Pool","Garden","Security","Lift"])
    submit=st.form_submit_button("Find Properties")
if submit:
    payload={"client_name":name,"location":location,"property_type":typ,"purpose":purpose,"budget":budget,"bedrooms":bedrooms,"min_area_sqft":min_area or None,"max_area_sqft":max_area or None,"amenities":amenities,"furnishing":None if furnishing=="Any" else furnishing}
    try:
        r=requests.post("http://127.0.0.1:8000/properties/plan",json=payload,timeout=20); r.raise_for_status(); data=r.json()
        st.success("Property plan generated.")
        st.subheader("Property Options"); st.json(data["properties"])
        st.subheader("Area Insights"); st.json(data["area_insights"])
        st.subheader("Site Visit"); st.write(data["property_visit"])
        st.subheader("Affordability Estimate"); st.write(data["affordability"])
        st.subheader("Validation"); st.write(data["validation"])
        st.caption(data["disclaimer"])
    except Exception as e: st.error(f"Backend unavailable: {e}")
