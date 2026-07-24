import streamlit as st
import requests

st.set_page_config(page_title="Kabitix AI", page_icon="🤖", layout="wide")

st.title("🤖 Kabitix AI")
st.write("Welcome to Kabitix AI!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_ai_response(prompt):
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
            json={"inputs": prompt},
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                return result[0]["generated_text"]
            return str(result)
        else:
            return f"Error: {response.status_code}"
    except Exception:
        return "Sorry, I couldn't connect to the AI."

if prompt := st.chat_input("Message Kabitix..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        reply = get_ai_response(prompt)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
