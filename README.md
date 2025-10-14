# AI Phone Bot (Twilio + Gemini)

An AI assistant that talks to you over a phone call using Twilio, Gemini API, and Flask!

## Features
- Make call from website
- Send instant voice messages: Type a message on the website, and it will be read out to the recipient over a phone call. Ideal for urgent messages that can't be missed.
- Record user's voice
- AI understands question and replies back via voice
- Continuous conversation loop

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Create `.env` file with your Twilio + Gemini keys.
3. Start Flask server: `python app.py`
4. Run Ngrok: `ngrok http 5000`
5. Configure Twilio Webhook to `https://your-ngrok-url/voice`
