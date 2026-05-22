import streamlit as st 

st.title("chai maker")

if st.button("make chai") :
    st.success(" your chai is being brewed")
add_masala = st.checkbox("add masala")
if add_masala: 
    st.write("masala added to your chai")

tea_type = st.radio(" pick your chai base:", ["MILK", "WATER", "ALMOND MILK"])

st.write(f"selected base { tea_type}")


flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])

st.write(f"Selected Flavour {flavour}")


sugar = st.slider("sugar level (spoon)" , 0, 5,3)
st.write(f"selected sugar level {sugar}")

cups = st.number_input("how many cups", min_value= 1 , max_value= 10 , step= 1)

name = st.text_input("enter your name")
if name :
     st.write(f"Welcome, {name}! Your chai is on the way")
     

dob = st.date_input("select your date of birth" )
st.write(f"your date of birth {dob}")