import os
from openai import OpenAI
from gtts import gTTS

def get_chatgpt_response(prompt, lang, f_name):
    
    client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY"),)
    
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",)
    
    response_text = chat_completion.choices[0].message.content
    tts = gTTS(response_text, lang=lang)
    tts.save(f_name+".mp3") 
    return response_text

def main():
    
    user_input = input("Please enter your message: ")
    user_lang= input("Please pick your language: ")
    f_name= input("Name your file: ")
    chatgpt_response = get_chatgpt_response(user_input, user_lang, f_name)


if __name__ == "__main__":
    main()

