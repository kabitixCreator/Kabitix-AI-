from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_image(image, question):

    if image is None:
        return "❌ Please upload an image."

    return f"""
🖼️ Image received successfully!

Question:
{question}

✅ The image has been uploaded correctly.

🚀 Real Vision AI will be connected in the next step.
After that Kabitix AI will be able to:

• Describe images
• Read text (OCR)
• Solve math from photos
• Explain biology diagrams
• Identify objects
• Answer questions about uploaded images
""" 
