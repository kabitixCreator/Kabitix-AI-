import streamlit as st

def welcome_cards():
    if st.button("💬 Chat with AI", use_container_width=True):
        st.session_state.page = "🤖 Chat"

    if st.button("📚 AI Study", use_container_width=True):
        st.session_state.page = "📚 AI Study"

    if st.button("🌍 Translator", use_container_width=True):
        st.session_state.page = "🌍 Translator"

    if st.button("📖 eBook Creator", use_container_width=True):
        st.session_state.page = "📚 eBook Creator"
