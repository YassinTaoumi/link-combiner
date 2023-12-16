import streamlit as st


st.title("Welcome to the link combiner for medium articles")

link = st.text_input("Enter your name")

if st.button("Generate link"):
    full_link = f"https://webcache.googleusercontent.com/search?q=cache:{link}"
    st.write(full_link)
