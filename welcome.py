import streamlit as st

def welcome_cards():
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:12px;margin-top:15px;">

        <div style="background:#1E293B;padding:18px;border-radius:15px;">
            💬 Chat with AI
        </div>

        <div style="background:#1E293B;padding:18px;border-radius:15px;">
            📚 AI Study
        </div>

        <div style="background:#1E293B;padding:18px;border-radius:15px;">
            🌍 Translator
        </div>

        <div style="background:#1E293B;padding:18px;border-radius:15px;">
            📖 eBook Creator
        </div>

    </div>
    """, unsafe_allow_html=True) 
