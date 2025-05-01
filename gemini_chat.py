import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

history = [
    {
        "role": "user",
        "parts": [
            {
                "text": '''You are My AI assistant. You will be talking to me like a human, like Iron Man's Jarvis. 
                           Remember you are talking on a call, answer in maximum of 4 lines.'''
            }
        ]
    }
]

def chat_with_gemini(user_input):

    global history

    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    chat = model.start_chat(history=history)
    response = chat.send_message(user_input,stream=True)
    response.resolve() # Ensure the response is fully generated

    history.append({"role" : "user","parts":[{"text":user_input}]})
    history.append({"role" : "assistant","parts":[{"text":response.text}]})

    return response.text