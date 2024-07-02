import openai
import os

def get_chatgpt_response(prompt):
    # Set the OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    
    # Create a chat completion using the openai library directly
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" depending on your subscription
        messages=[{"role": "user", "content": prompt}]
    )

    # Print the raw response from OpenAI (optional)
    print(chat_completion)

    # Extract and return the text of the response
    response_text = chat_completion.choices[0].message['content']
    return response_text

def main():
    # Take user input
    user_input = input("Please enter your message: ")

    # Get response from ChatGPT
    chatgpt_response = get_chatgpt_response(user_input)

    # Print the response
    print("ChatGPT Response:", chatgpt_response)

if __name__ == "__main__":
    main()

