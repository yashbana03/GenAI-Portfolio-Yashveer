import streamlit as st 
import requests 
st.title("live currency convertor")
amount = st.number_input("enter the amount in INR:", min_value=1)

target_currency = st.selectbox("CONVERT TO:",["USD", "JPY", "EUR", "GBD"])

if st.button("conver") :
    url= "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    
    if response.status_code==200 :
        data = response.json()
        rate= data["rates"][target_currency]
        converted = rate*amount
        st.success(f"{amount} INR = {converted:.2F} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")





