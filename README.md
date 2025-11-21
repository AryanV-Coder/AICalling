# Vayu — Voice-First AI Assistant

A full-stack AI assistant that enables real-time phone conversations with AI. Have natural voice interactions by simply providing your phone number — just like calling a person.

## Tech Stack
- **Frontend:** HTML/CSS
- **Backend:** Flask
- **AI:** Google Gemini
- **Voice:** Twilio

## Features
- **Real-time AI Phone Conversations:** Call the AI and have natural voice interactions
- **Speech-to-Text & Text-to-Speech:** Seamless voice processing pipelines
- **Emergency Message Delivery:** Send urgent messages via phone call when you can't call directly and need instant delivery
  - Enter recipient's phone number and message
  - AI calls them and speaks your message aloud
  - Perfect for time-sensitive situations where texts might be missed
- **Conversational Memory:** AI maintains context throughout the conversation

## Setup

### Prerequisites
- Python 3.8+
- Twilio account (with Account SID, Auth Token, and phone number)
- Google Gemini API key
- ngrok (for local development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AryanV-Coder/AICalling.git
   cd AICalling
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_NUMBER=your_twilio_phone_number
   GEMINI_API_KEY=your_gemini_api_key
   RENDER_URL=your_ngrok_or_deployment_url
   ```

5. **Start the Flask server**
   ```bash
   python app.py
   ```

6. **Set up ngrok (for local development)**
   ```bash
   ngrok http 5000
   ```
   Copy the ngrok URL (e.g., `https://xxxx.ngrok.io`) and update `RENDER_URL` in your `.env` file.

7. **Configure Twilio webhook**
   - Go to your Twilio Console
   - Navigate to your phone number settings
   - Set the voice webhook URL to: `https://your-ngrok-url/voice`

8. **Access the application**
   
   Open your browser and go to `http://localhost:5000`

## Usage

### For AI Conversations
1. Open the web interface
2. Enter your phone number
3. Leave the message field empty
4. Click "Connect Now"
5. Answer the incoming call and start talking with the AI

### For Emergency Messages
1. Open the web interface
2. Enter the recipient's phone number
3. Type your urgent message
4. Click "Connect Now"
5. The recipient will receive a call with your message

## Future Scope
- Context-aware multi-agent system for specialized tasks
- Autonomous call screening and response handling
- Action-oriented autonomy (ordering, tracking, scheduling)
- Multi-user platform with authentication