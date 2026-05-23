import streamlit as st 
st.title("chai taste poll")

col1 , col2 = st.columns(2)
with col1 :
    st.header("masala chai")
    vote1 = st.button("VOTE MASALA CHAI")
with col2 : 
    st.header("adarak chai")
    vote2 = st.button("VOTE ADARAK CHAI")
    
if vote1:
    st.success("thanks for voting masala chai ")
elif vote2:
    st.success("thanks for voting adrak chai") 
    