import streamlit as st
import requests

st.title("Product Price Recommendation Chatbot")

product_name = st.text_input("Enter product name:")
if st.button("Get Price Recommendation"):
    if product_name:
        response = requests.get(f'http://localhost:8000/recommend/{product_name}')
        if response.status_code == 200:
            result = response.json()
            st.json(result)
        else:
            st.warning("Error fetching price recommendation.")
    else:
        st.warning("Please enter a product name.")