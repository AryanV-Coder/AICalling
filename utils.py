import requests
import speech_recognition as sr
import os
import time
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

def download_audio(recording_url):
    twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_token = os.getenv("TWILIO_AUTH_TOKEN")

    twilio_wav = "static/audio/twilio_original.wav"
    processed_wav = "static/audio/recording.wav"

    try:
        time.sleep(2)  # Give Twilio time to finalize recording

        # ✅ Download with Basic Auth
        response = requests.get(recording_url + ".wav", auth=(twilio_sid, twilio_token))
        if response.status_code != 200:
            raise Exception(f"Failed to download recording. Status code: {response.status_code}")
        
        with open(twilio_wav, 'wb') as f:
            f.write(response.content)
        print("[✅] Downloaded Twilio recording")

        # 🎧 Convert to 16kHz mono WAV for transcription
        audio = AudioSegment.from_file(twilio_wav, format="wav")
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export(processed_wav, format="wav")
        print("[✅] Converted audio to proper format")

        return processed_wav

    except Exception as e:
        print("🔥 ERROR in download_audio():", e)
        return None


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        text = "Sorry, I could not understand."
    return text
