import os
from openai import OpenAI
from gtts import gTTS

def get_chatgpt_response(prompt): 
    api_key = os.environ.get("OPENAI_API_KEY")
    
    client = OpenAI(api_key=api_key,)
  
    chat_completion = client.chat.completions.create( 
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",)

    response_content = chat_completion.choices[0].message.content
    tts = gTTS(response_content, lang='en')
    file_path = 'output.mp3'
    if os.path.exists(file_path):
        os.remove(file_path)  
    tts.save("output.mp3")  
    
    return response_content

def main():
    
    user_input = input("Please enter your message: ")
    
    chatgpt_response = get_chatgpt_response(user_input)
    
    #print("ChatGPT Response:", chatgpt_response)

if __name__ == "__main__":
    main()


