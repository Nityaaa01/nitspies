import streamlit as st
st.title("Welcome to the Streamlit")
name = st.text_input("Enter your name")
if name: 
    st.success(f"Hello {name}!")
age= st.slider("Select your age", 0, 100, 25)
st.write(f"Age: {age}")
if st.button("Celebrate"): st.balloons()  