import streamlit as st
import requests

st.set_page_config(
    page_title="Project Intelligence Assistant",
    layout="wide"
)

st.title("Project Intelligence Assistant")

question = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "question": question
        }
    )

    answer = response.json()["answer"]

    st.markdown(answer)