import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Purna AI App")
st.title("🎈 Purna AI Assistant")
st.write("Nee Doubt Adugu Purna!")

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

question = st.text_input("Em Adagali anukuntunnav?")

if st.button("Adugu"):
    if question:
        with st.spinner("Alochistunna..."):
            response = model.generate_content(question)
            st.success(response.text)
    else:
        st.warning("Question raayi Purna!")
