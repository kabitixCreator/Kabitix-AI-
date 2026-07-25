import streamlit as st

def study_page():
    st.title("📚 AI Study Mode")

    text = st.text_area(
        "Paste your notes here",
        height=250,
        placeholder="Paste your study notes..."
    )

    if st.button("✨ Generate Summary"):
        if text:
            st.success("Summary feature will be connected to AI next.")
        else:
            st.warning("Please paste your notes first.") 
