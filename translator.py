import streamlit as st
from chatbot import get_ai_response

def translator_page():
    st.title("🌍 AI Translator")

    text = st.text_area(
        "Enter text",
        height=180,
        placeholder="Type anything..."
    )

    language = st.selectbox(
        "Translate To",
        [
            "English",
            "Hindi",
            "Bengali",
            "Assamese",
            "Khasi",
            "Garo",
            "Nagamese",
            "French",
            "Spanish",
            "Japanese"
        ]
    )

    if st.button("🌐 Translate"):

        if not text.strip():
            st.warning("Please enter some text.")
            return

        prompt = f"""
Translate the following text into {language}.

Only return the translated text.

Text:
{text}
"""

        with st.spinner("🌍 Translating..."):
            result = get_ai_response(prompt)

        st.success("Translation Complete!")
        st.markdown(result)

        st.download_button(
            "📥 Download Translation",
            result,
            file_name="translation.txt"
        )
