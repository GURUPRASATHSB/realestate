from app.tools.property_loan_calculator import estimate_affordability
def test_loan():
    x=estimate_affordability(6500000)
    assert x["estimated_loan_amount"]==5200000
    assert x["estimated_monthly_emi"]>0
