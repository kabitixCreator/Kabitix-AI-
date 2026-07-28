from groq import Groq
import os
import base64

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_image(image, question):

    if image is None:
        return "❌ Please upload an image."

    image_bytes = image.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content
