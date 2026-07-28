from groq import Groq
from tavily import TavilyClient
import os

# API Clients
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def get_ai_response(prompt):
    try:
        # Search the web
        search = tavily.search(query=prompt)

        web_info = ""

        if search.get("results"):
            for result in search["results"][:3]:
                web_info += result.get("content", "") + "\n\n"

        # Ask Groq using web information
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are Kabitix, a helpful, intelligent and friendly AI assistant.

Use the following live web information if it is relevant.

{web_info}
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
