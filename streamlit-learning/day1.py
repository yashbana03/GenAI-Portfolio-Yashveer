import streamlit as st 
st.title(" Hello Chai App")
st.subheader("brewed with streamlit")
st.text("welcome to your first interactive app")
st.write("choose your fav. type of chai")
li =["masala chai", " lemon chai " , "kesasr chai "]
chai = st.selectbox("your fav chai : " , li )
st.write(f"your choice {chai}. badiya hai choose kiya hai ")
st.success("your chai has been brewed")