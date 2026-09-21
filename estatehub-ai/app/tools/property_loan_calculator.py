def estimate_affordability(price,budget=None,down_payment_rate=0.20,annual_rate=8.5,years=20):
    down=price*down_payment_rate
    loan=price-down
    r=annual_rate/12/100
    n=years*12
    emi=loan*r*(1+r)**n/((1+r)**n-1) if r else loan/n
    return {"property_price":price,"down_payment":round(down,2),"estimated_loan_amount":round(loan,2),"estimated_monthly_emi":round(emi,2),"within_budget":None if budget is None else price<=budget}
