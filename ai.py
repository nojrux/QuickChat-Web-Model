from openai import OpenAI
import os

os.getenv("MY_SECRET")

client = OpenAI(
    api_key=MY_SECRET,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chatbot(messages):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages
    )
    return response.choices[0].message.content

