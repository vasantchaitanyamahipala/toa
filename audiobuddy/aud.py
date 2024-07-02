import requests
import os
from openai import OpenAI
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream, save
from elevenlabs.client import ElevenLabs

def get_chatgpt_response(prompt, lang, f_name, spl, saveinfo):
    
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
    print(response_text)
    if spl=="F" or spl=="f":
    	tts = gTTS(response_text, lang=lang)
    	tts.save(f_name+".mp3")
    else:
        synthesize_text(response_text, lang, saveinfo, f_name) 

def synthesize_text(text, language, saveinfo, f_name):
    
    client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))
    voice=input("Pick your choice of voice: ")
    audio = client.generate(
    text=text,
    voice="Rachel",
    model="eleven_multilingual_v2")
    play(audio)
    if saveinfo=="T" or saveinfo=="t":
        save(audio, f_name+".mp3")


def main():
    
    user_input = input("Please enter your message: ")
    user_lang= input("Please pick your language: ")

    spl=input("Eleven labs Version T/F: ")
    saveinfo=input("Do you want to save the file T/F: ")
    if saveinfo=="T" or saveinfo=="t":
        f_name=input("Please name your file: ")
    else:
        f_name=None
    chatgpt_response = get_chatgpt_response(user_input, user_lang, f_name, spl, saveinfo)


if __name__ == "__main__":
    main()


