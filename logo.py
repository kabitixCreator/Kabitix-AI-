import streamlit as st

def show_logo():
    st.markdown("""
    <div style="text-align:center;padding:5px 0 10px 0;">
        <h1 style="
            color:white;
            font-size:48px;
            margin-bottom:5px;
        ">
            🤖 Kabitix AI
        </h1>

        <p style="
            color:#8B949E;
            font-size:18px;
            margin-top:0;
        ">
            Smart • Fast • Simple
        </p>
    </div>
    """, unsafe_allow_html=True) 
