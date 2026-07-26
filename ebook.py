import streamlit as st

def ebook_page():
    st.title("📖 AI eBook Creator")

    title = st.text_input("Book Title")
    topic = st.text_area("Book Topic")

    if st.button("✨ Generate eBook"):
        if title and topic:
            ebook = f"""
# {title}

## Introduction
This eBook is about {topic}.

## Chapter 1
{topic} is an important subject.

## Chapter 2
Here you can write more content about {topic}.

## Conclusion
Thank you for reading this eBook.
"""

            st.success("✅ eBook Generated!")
            st.markdown(ebook)

            st.download_button(
                "⬇ Download eBook",
                ebook,
                file_name=f"{title}.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please enter a title and topic.")
