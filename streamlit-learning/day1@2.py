import streamlit as st 
st.title("mission defence app")
st.subheader("choose your aim")
exam = st.selectbox("select only one target:" , [ "CDS", "AFCAT"])
if exam == "AFCAT": 
    st.write("🔥 **AFCAT (8 Aug):** Bhai, Maths aur Reasoning tight kar le, is baar cutoff clear karna hai!")
    st.success("Best of Luck! Tera Uniform taiyar ho raha hai.")
if exam == "CDS" :
    st.write("📚 **CDS (13 Sept):** English aur GS par pakad banao, UPSC level ka paper aayega!")
    st.success("Jai Hind! Taiyari mein koi kami nahi honi chahiye.")