import streamlit as st 
from datetime import date 

st.title("🎂 Age Calculator App")
st.subheader("Apni Date of Birth daalo aur age dekho!")


today = date.today()
dob = st.date_input(
        "Apni Date of Birth (DOB) select karo:", 
        value=date(2000,1,1), 
        min_value= date(1920, 1, 1),
        max_value = today 
)
if dob:
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age = age - 1
        
    st.write(f"📅 Aapki Date of Birth hai: {dob}")
    st.success(f"🎉 Bhai, aapki umar abhi **{age} Saal** hai!")