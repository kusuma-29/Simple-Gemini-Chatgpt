# Simple-Gemini-Chatgpt

This is a simple command-line chatbot built using Google's Generative AI model (Gemini 1.5 Flash). It allows you to interact with Gemini in plain text using your API key.

## 🔧 Features

- Simple CLI-based conversation
- Responses are plain text (no markdown or formatting)
- Stops when you type `exit`

## 🚀 Requirements

- Python 3.7 or later
- Google Generative AI Python SDK

## 📦 Installation

1. Clone the repository:

git clone https://github.com/your-username/gemini-chat-cli.git
cd gemini-chat-cli

2. Install the required package:

pip install google-generativeai

## 🔑 Set Up API Key

Replace the `API_KEY` in the script with your actual API key from Google AI Studio:
```python
API_KEY = "your-api-key-here"

🧠 Run the Chatbot
python gemini_chat.py

Then type your messages. To exit the conversation, type:
exit

Code Output:

🧑 You: Hello
🤖 Gemini: Hi there! How can I help you today?

🧑 You: Tell me a fun fact.
🤖 Gemini: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.

🧑 You: Who is the president of India?
🤖 Gemini: As of 2025, the President of India is Droupadi Murmu.
