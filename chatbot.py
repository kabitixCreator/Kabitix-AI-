from groq import Groq
from tavily import TavilyClient
from memory import load_memory, save_memory, remember
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def get_ai_response(prompt, pdf_text=""):

    try:

        memory = load_memory()

        prompt_lower = prompt.lower()


        # ---------- MEMORY ----------

        if "my name is" in prompt_lower:
            name = prompt.split("my name is")[-1].strip()

            memory["name"] = name
            save_memory(memory)

            return f"Nice to meet you, {name}! I will remember your name."

        if "what is my name" in prompt_lower or "who am i" in prompt_lower:

            if "name" in memory:
                return f"Your name is {memory['name']}."

            return "I don't know your name yet."



        if "i live in" in prompt_lower:

            place = prompt.split("i live in")[-1].strip()

            remember("place", place)

            return f"Okay! I'll remember that you live in {place}."



        if "where do i live" in prompt_lower:

            if "place" in memory:
                return f"You live in {memory['place']}."

            return "I don't know where you live yet."
    
        if "i study in" in prompt_lower:

            study = prompt.split("i study in")[-1].strip()

            remember("study", study)

            return f"Got it! I'll remember that you study in {study}."


        if "what do i study" in prompt_lower or "where do i study" in prompt_lower:

            if "study" in memory:
                return f"You study in {memory['study']}."

            return "I don't know what you study yet."


        # ---------- LIVE SEARCH ----------

        search = tavily.search(
            query=prompt,
            search_depth="advanced",
            max_results=5,
            include_answer=True
        )

        web_info = ""

        if search.get("results"):
        for result in search["results"]:
                web_info += (
                    f"Title: 
        {result.get('title','')}\n"
                    f"Content: 
        {result.get('content','')}\n"
                    f"URL: 
        {result.get('url','')}\n\n"
                )
         response =
         client.chat.completions.create(
         
         model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are Kabitix AI, a smart, friendly and helpful AI assistant.

Always use the live Tavily search results if they are relevant.

If a PDF has been uploaded, use the PDF content to answer whenever possible.

Memory:
Name: {memory.get('name','')}
Place: {memory.get('place','')}
Study: {memory.get('study','')}

Live Search Results:

{web_info}

PDF Content:

{pdf_text}
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
def speech_to_text(audio_file):
    try:
        with open(audio_file, "rb") as file:
            transcript = client.audio.transcriptions.create(
                file=file,
                model="whisper-large-v3"
            )

        return transcript.text

    except Exception as e:
        return f"Error: {e}" 
