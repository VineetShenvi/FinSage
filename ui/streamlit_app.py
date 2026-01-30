import streamlit as st
import requests

st.set_page_config(page_title="Investment Research AI")

st.title("📈 Autonomous Investment Research")

company = st.text_input("Enter company name")

if st.button("Analyze"):
    with st.spinner("Running agent workflow..."):
        res = requests.post(
            "http://localhost:8000/analyze",
            json={"company": company}
        ).json()

    st.subheader("📊 Financial Analysis")
    st.write(res["financial_analysis"])

    st.subheader("🧠 Investment Thesis")
    st.write(res["investment_thesis"])
