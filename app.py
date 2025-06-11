import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_community.chat_models import ChatGoogleGenerativeAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page layout
st.set_page_config(
    page_title="Zoho ChatBot",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customize sidebar appearance
st.markdown("""
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """, unsafe_allow_html=True)

# Set up Google API key
if 'GOOGLE_API_KEY' not in st.session_state:
    st.session_state.GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Create sidebar with title
st.sidebar.title("Configuration")

# Add API key input to sidebar
api_key_input = st.sidebar.text_input(
    "Google API Key",
    type="password",
    placeholder="Paste your Google API key here",
    value=st.session_state.GOOGLE_API_KEY if 'GOOGLE_API_KEY' in st.session_state else '',
    key="api_key_input"
)

if api_key_input:
    st.session_state.GOOGLE_API_KEY = api_key_input
    os.environ['GOOGLE_API_KEY'] = api_key_input

if not st.session_state.GOOGLE_API_KEY:
    st.error("Please add your Google API key to continue!")
    st.stop()

# Set up the chat model and conversation chain
if 'chat_model' not in st.session_state:
    st.session_state.chat_model = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.7
    )

if 'conversation' not in st.session_state:
    st.session_state.conversation = ConversationChain(
        llm=st.session_state.chat_model,
        memory=ConversationBufferMemory()
    )

# Set page title
st.title("Zoho ChatBot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.conversation.predict(input=prompt)
            st.markdown(response)
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})