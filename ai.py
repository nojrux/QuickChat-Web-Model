import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("MY_SECRET"))

def chatbot(messages):
    system_instruction = ""
    converted = []

    # Extract system message + convert others
    for msg in messages:
        role = msg["role"]

        if role == "system":
            system_instruction = msg["content"]
            continue

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

    # IMPORTANT: create a model with the current system_instruction
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction
    )

    # Now call generate_content WITHOUT system_instruction
    response = model.generate_content(
        converted
    )

    return response.text
