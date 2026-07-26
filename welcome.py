import streamlit as st

def welcome_cards():
    st.markdown("""
    <div style="margin-top:20px;"></div>

    <div style="
        background:#161B22;
        padding:15px;
        border-radius:15px;
        margin-bottom:10px;
        color:white;
        font-size:18px;
    ">
    💬 Chat with AI
    </div>

    <div style="
        background:#161B22;
        padding:15px;
        border-radius:15px;
        margin-bottom:10px;
        color:white;
        font-size:18px;
    ">
    📚 AI Study
    </div>

    <div style="
        background:#161B22;
        padding:15px;
        border-radius:15px;
        margin-bottom:10px;
        color:white;
        font-size:18px;
    ">
    🌍 Translator
    </div>

    <div style="
        background:#161B22;
        padding:15px;
        border-radius:15px;
        color:white;
        font-size:18px;
    ">
    📖 eBook Creator
    </div>
    """, unsafe_allow_html=True) 
