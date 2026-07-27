from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_image(image_base64, question):
    return """
🖼️ Image Vision is coming soon!

Kabitix AI will soon be able to:

✅ Describe images
✅ Read text (OCR)
✅ Solve math from photos
✅ Explain biology diagrams
✅ Identify objects
✅ Answer questions about uploaded images

This feature is under development.
""" 
