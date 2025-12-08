import os
import google.generativeai as genai


genai.configure(api_key=os.environ.get("MY_SECRET"))
model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot(messages):
    # Convert OpenAI-style messages to Gemini-style
    converted = []
    for msg in messages:
        converted.append({
            "role": msg["role"],
            "parts": [
                {"text": msg["content"]}
            ]
        })

    response = model.generate_content(converted)
    return response.text

