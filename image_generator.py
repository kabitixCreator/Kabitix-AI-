import requests
import os

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-dev"

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
