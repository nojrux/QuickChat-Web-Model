from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDD9qTnEM7FWBW3jDRbHqjsjg8lAMRJR6I",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chatbot(messages):
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=messages
    )
    return response.choices[0].message.content

