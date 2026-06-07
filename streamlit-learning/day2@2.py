import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file  = st.file_uploader("UPload your csv file", type=["csv", "xlsx"])

if file is not None:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    
    
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    job = df["Job Title"].unique()
    selected_job = st.selectbox("Filter by job type", job)
    filtered_data = df[df["Job Title"] == selected_job]
    st.dataframe(filtered_data)
     

if file:
    job = df["Sex"].unique()
    selected_job = st.selectbox("Filter by job type", job)
    filtered_data = df[df["Sex"] == selected_job]
    
    st.dataframe(filtered_data)