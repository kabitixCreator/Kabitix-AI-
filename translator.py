import streamlit as st

def translator_page():
    st.title("🌍 AI Translator")

    text = st.text_area("Enter text")

    language = st.selectbox(
        "Translate To",
        [
            "Hindi",
            "English",
            "Bengali",
            "Assamese",
            "Khasi",
            "Garo",
            "Nagamese"
        ]
    )

    if st.button("🌐 Translate"):
        if text:
            st.success(f"Translated to {language}")
            st.info(
                "⚠ Translation AI will be connected in the next update.\n\n"
                f"Original Text:\n\n{text}"
            )
        else:
            st.warning("Please enter some text.")
