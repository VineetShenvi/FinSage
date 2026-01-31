import streamlit as st
import requests

from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("BACKEND_URL")
print(uri)

st.set_page_config(page_title="Investment Research AI")

st.title("📈 Autonomous Investment Research")

company = st.text_input("Enter company name")

if st.button("Analyze"):
    with st.spinner("Running agent workflow..."):
        response = requests.post(
        uri,
        json={"company": company},
        timeout=30
        )
        try:
            res = response.json()
        except ValueError:
            
            st.error("Response was not valid JSON")
            st.text(response.text)
            st.stop()

    st.subheader("📊 Financial Analysis")
    st.write(res["financial_analysis"])

    st.subheader("🧠 Investment Thesis")
    st.write(res["investment_thesis"])
