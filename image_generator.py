from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_image_prompt(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "Convert the user's request into a detailed, high-quality "
                    "image generation prompt."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content 
