import streamlit as st
import requests
from groq import Groq
import os
st.set_page_config(page_title="Kabitix AI", page_icon="🤖", layout="wide")

st.title("🤖 Kabitix AI")
st.write("Welcome to Kabitix AI!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are Kabitix AI, a helpful, intelligent, and friendly AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

if prompt := st.chat_input("Message Kabitix..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        reply = get_ai_response(prompt)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
