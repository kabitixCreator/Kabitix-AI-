from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.environ.get("HF_TOKEN")

@app.route("/")
def home():
    return "✅ Kabitix AI Backend is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list):
            reply = result[0].get("generated_text", "No response")
        else:
            reply = str(result)
        return jsonify({"reply": reply})

    return jsonify({"reply": "Error connecting to AI."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
