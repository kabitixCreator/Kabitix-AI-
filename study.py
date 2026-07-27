import streamlit as st
from chatbot import get_ai_response

def study_page():
    st.title("📚 AI Study Mode")

    notes = st.text_area(
        "Paste your notes here",
        height=250,
        placeholder="Paste your notes..."
    )

    option = st.selectbox(
        "Choose",
        [
            "Summary",
            "Important Points",
            "MCQs",
            "Short Questions & Answers"
        ]
    )

    if st.button("✨ Generate"):

        if not notes.strip():
            st.warning("Please paste some notes first.")
            return

        with st.spinner("🤖 Kabitix is studying your notes..."):

            if option == "Summary":
                prompt = f"""
Summarize these notes in simple language.

Notes:
{notes}
"""

            elif option == "Important Points":
                prompt = f"""
Extract the most important points from these notes.

Notes:
{notes}
"""

            elif option == "MCQs":
                prompt = f"""
Create 10 multiple choice questions with answers from these notes.

Notes:
{notes}
"""

            else:
                prompt = f"""
Create short questions and answers from these notes.

Notes:
{notes}
"""

            result = get_ai_response(prompt)

        st.success("Done!")
        st.markdown(result)

        st.download_button(
            "📥 Download",
            result,
            file_name="study_notes.txt"
        )
