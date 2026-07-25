import streamlit as st
from groq import Groq
import os
from chatbot import get_ai_response
from ebook import ebook_page
from study import study_page
from translator import translator_page
from settings import settings_page
from utils import apply_theme
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
st.sidebar.title("🤖 KTIX") 
if st.sidebar.button("➕ New Chat"):
    if st.session_state.messages:
        st.session_state.history.append(st.session_state.messages.copy())
    st.session_state.messages = []
    st.rerun() 
 with st.sidebar.expander("📜 History", expanded=True):
    for i, chat in enumerate(st.session_state.history):
        title = chat[0]["content"][:20] + "..." if chat else f"Chat {i+1}"

        if st.button(f"💬 {title}", key=f"history_{i}"):
            st.session_state.messages = chat
            st.rerun() 
page = st.sidebar.radio(
    "📂 Menu",
    [
        "🤖 Chat",
        "📚 AI Study",
        "📚 eBook Creator",
        "🌍 Translator",
        "⚙️ Settings"
    ]
) 

apply_theme()
elif page == "📚 AI Study":
    study_page() 
if page == "📚 eBook Creator":
    ebook_page()
    st.stop()

elif page == "🌍 Translator":
    translator_page()
    st.stop() 

elif page == "⚙️ Settings":
    settings_page()
    st.stop() 
if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = [] 

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
uploaded_image = st.file_uploader(
    "📷 Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
prompt = st.chat_input("💬 Ask anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
    st.markdown(prompt)

with st.chat_message("assistant"):
    with st.spinner("🤖 Kabitix is thinking..."):
        reply = get_ai_response(prompt)
    st.markdown(reply)
    st.code(reply, language=None) 

st.session_state.messages.append({
    "role": "assistant",
    "content": reply
}) 
