import requests
import os

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell" 

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Content-Type": "application/json"
}

def generate_image(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt
        }
    )

    if response.status_code == 200:
        return response.content

    print(response.status_code)
    print(response.text)
    return None 
