# Zoho Support Chatbot

An AI-powered chatbot that helps users with Zoho app setup and support by fetching information from Zoho's documentation.

## Setup

1. Create a virtual environment (already done):
   ```
   python -m venv venv
   ```

2. Install dependencies (already done):
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Rename `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file

## Running the Chatbot

To start the chatbot:
```
streamlit run app.py
```

## Features

- Select from multiple Zoho apps (CRM, Books, Mail, Projects, etc.)
- Natural language conversation using OpenAI's GPT models
- Real-time documentation fetching from Zoho's help pages
- Conversation memory to maintain context
- Easy app switching during conversations

## Usage

1. Start the application
2. Select the Zoho app you need help with
3. Ask your questions naturally
4. Switch between different Zoho apps as needed