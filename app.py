#For development -> ngrok http 5000
from flask import Flask, request, Response, render_template, redirect
from gemini_chat import chat_with_gemini
from tts_engine import text_to_speech
import utils
from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests
import urllib.parse

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def call():
    phone_number = request.form['phone_number']
    message = request.form['message']
    call_user(phone_number,message)
    return redirect('/')

@app.route('/voice', methods=['POST'])
def voice():
    return Response(
        """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Polly.Matthew">Hello! I am your AI Assistant. Please speak after the beep.</Say>
  <Record maxLength="10" timeout="4" action="/process_recording" />
</Response>""",
        mimetype='text/xml'
    )

@app.route('/process_recording', methods=['POST'])
def process_recording():
    try:
        recording_url = request.form['RecordingUrl']
        print("✅ [Recording URL]", recording_url)

        audio_path = utils.download_audio(recording_url)
        print("✅ [Downloaded File]", audio_path)

        text = utils.transcribe_audio(audio_path)
        print("✅ [Transcribed Text]", text)

        if text == "Unknown":
            ai_reply = "Sorry I could not understand !! Kindly speak again !!"
        else:
            ai_reply = chat_with_gemini(text)
        print("✅ [Gemini Reply]", ai_reply)

        audio_file_url = text_to_speech(ai_reply)
        print("✅ [TTS URL]", audio_file_url)

        # # ✅ Ensure audio URL is reachable
        # head_response = requests.head(audio_file_url, timeout=3)
        # if head_response.status_code != 200:
        #     raise Exception(f"TTS file not accessible: HTTP {head_response.status_code}")

        # ✅ Respond with audio and loop
        twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Play>{audio_file_url}</Play>
  <Pause length="1"/>
  <Record maxLength="10" timeout="4" action="/process_recording" />
</Response>"""

        return Response(twiml, mimetype='text/xml', status=200)

    except Exception as e:
        print("🔥 ERROR in /process_recording:", e)
        return Response(
            """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Sorry, something went wrong while responding. Please try again later.</Say>
  <Redirect>/voice</Redirect>
</Response>""",
            mimetype='text/xml',
            status=200
        )

@app.route('/send-message', methods=['POST'])
def send_message():

    user_message = request.args.get('message', '')
    decoded_message = urllib.parse.unquote(user_message)
    print(decoded_message)

    return Response(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Polly.Matthew">{decoded_message}</Say>
</Response>""",
        mimetype='text/xml'
    )

def call_user(user_number,user_message):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    client = Client(account_sid, auth_token)

    if user_message.strip() == "":
        call = client.calls.create(
            to="+91"+user_number,
            from_=twilio_number,
            url=f"{os.getenv('RENDER_URL')}/voice"
        )
        return call.sid
    
    else :
        # URL encode the message to handle special characters
        print(user_message)
        encoded_message = urllib.parse.quote(user_message)
        print(encoded_message)
        call = client.calls.create(
                to="+91"+user_number,
                from_=twilio_number,
                url=f"{os.getenv('RENDER_URL')}/send-message?message={encoded_message}"
            )
        return call.sid

if __name__ == "__main__":
    app.run(port=5000,debug = True)