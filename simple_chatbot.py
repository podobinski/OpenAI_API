from openai import OpenAI
import json

# Load the API keys from the json file
with open('api_keys.json') as f:
    keys = json.load(f)

# Instantiate a client
client = OpenAI(api_key=keys["openai_api_key"])


messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.9,
        max_tokens=150,
    )
    messages.append({"role": "assistant", "content": chat_response.choices[0].message.content})
    print("Assistant:", chat_response.choices[0].message.content)
    print("")
