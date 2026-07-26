import streamlit as st
from chatbot import get_ai_response
from ebook import ebook_page
from translator import translator_page
from settings import settings_page
from study import study_page
from utils import apply_theme
from logo import show_logo
st.set_page_config(
    page_title="Kabitix AI",
    page_icon="🤖",
    layout="centered"
)

apply_theme()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

show_logo() 

if st.sidebar.button("➕ New Chat"):
    if st.session_state.messages:
        st.session_state.history.append(
            st.session_state.messages.copy()
        )
    st.session_state.messages = []
    st.rerun() 

with st.sidebar.expander("📜 History", expanded=True):
    for i, chat in enumerate(st.session_state.history):
        title = (
            chat[0]["content"][:20] + "..."
            if chat else f"Chat {i+1}"
        )

        if st.button(
            f"💬 {title}",
            key=f"history_{i}"
        ):
            st.session_state.messages = chat
            st.rerun()

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
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

if page == "📚 AI Study":
    study_page()
    st.stop()

elif page == "📚 eBook Creator":
    ebook_page()
    st.stop()

elif page == "🌍 Translator":
    translator_page()
    st.stop()

elif page == "⚙️ Settings":
    settings_page()
    st.stop() 
st.title("🤖 Kabitix AI")
st.markdown(
    "<p style='text-align:center;color:#8B949E;'>The Future of Smart AI</p>",
    unsafe_allow_html=True
) 

uploaded_image = st.file_uploader(
    "📷 Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("💬 Ask anything...")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Kabitix is thinking..."):
            reply = get_ai_response(prompt)

        st.markdown(reply)
        st.code(reply, language=None)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    ) 
