import streamlit as st
from groq import Groq
import os

st.set_page_config(
    page_title="Kabitix AI",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp{
    background:#0B0F19;
}
h1{
    color:white;
    text-align:center;
}
p{
    color:#A5B4FC;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 Kabitix AI</h1>", unsafe_allow_html=True)
st.markdown("<p>How can I help you today?</p>", unsafe_allow_html=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are Kabitix AI, a helpful and friendly AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

prompt = st.chat_input("💬 Ask anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_ai_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
