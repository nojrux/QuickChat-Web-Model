from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDTGnW_R81KfpXMxOGfliLLrROPc9IRyvw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chatbot(messages):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages
    )
    return response.choices[0].message.content

