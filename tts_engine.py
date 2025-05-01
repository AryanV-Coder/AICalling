from gtts import gTTS
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

def text_to_speech(text):
    filename = f"static/audio/{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    public_url = f"https://aicalling-jd08.onrender.com/{filename}"
    return public_url