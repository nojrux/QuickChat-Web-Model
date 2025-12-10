import os
import google.generativeai as genai

#genai.configure(api_key=os.environ.get("MY_SECRET"))
genai.configure(api_key="AIzaSyAb1pXeF8PKeUYYuxqzRjt9AFLmuWO4cm8")

def chatbot(messages):
    system_instruction = ""
    converted = []

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

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction
    )

    response = model.generate_content(
        converted
    )

    return response.text
