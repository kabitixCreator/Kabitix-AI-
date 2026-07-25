import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    .stApp{
        background:#0B0F19;
    }

    h1,h2,h3{
        color:white;
    }

    p,label{
        color:#C9D1D9;
    }

    .stButton>button{
        width:100%;
        border-radius:12px;
    }

    .stChatInput{
        border-radius:20px;
    }
    </style>
    """, unsafe_allow_html=True)
