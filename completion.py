from openai import OpenAI
import json

# Load the API keys from the json file
with open('api_keys.json') as f:
    keys = json.load(f)

# Instantiate a client
client = OpenAI(api_key=keys["openai_api_key"])

# Create a chat completion request using the instantiated client
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use the correct chat model
    messages=[
        {"role": "user", "content": "What is the OpenAI API?"}
    ]
)

# Accessing the result
print(completion.choices[0].message.content)

