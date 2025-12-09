import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("MY_SECRET"))

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def chatbot(messages):

    # Split system message from conversation
    system_instruction = ""
    converted = []

    for msg in messages:

        role = msg["role"]

        # Gemini does NOT accept `"system"` inside the message list
        if role == "system":
            system_instruction = msg["content"]
            continue

        # Convert OpenAI → Gemini
        if role == "assistant":
            role = "model"
        elif role == "user":
            role = "user"
        else:
            role = "user"

        converted.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })

    # Generate response
    response = model.generate_content(
        converted,
        system_instruction=system_instruction
    )

    return response.text
