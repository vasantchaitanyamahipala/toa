import openai
import os

# Ensure your API key is correctly set in the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Using the openai.ChatCompletion.create function directly
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4", depending on your API plan
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ]
)

# Printing the entire completion object to see the structure
print(chat_completion)

# Extracting the text of the response
response_text = chat_completion['choices'][0]['message']['content']
print("Response from ChatGPT:", response_text)

