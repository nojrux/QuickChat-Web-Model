from openai import OpenAI
import os

MY_SECRET = os.environ.get("MY_SECRET")

client = OpenAI(
    api_key=MY_SECRET,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chatbot(messages):
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=messages
    )
    return response.choices[0].message.content

