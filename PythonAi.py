import streamlit as st
from google import genai

# Custom CSS injection for the Send button
st.markdown(
    """
    <style>
    div.stButton { text-align: center; }
    div.stButton > button {
        background-color: #4CAF50;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 32px !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease 0s;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #45a049 !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    div.stButton > button:active {
        transform: translateY(1px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header UI
st.markdown(
    """
    <h1 style='text-align: center;'> Python AI Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
    Ask any Python programming question.
    </p>
    """,
    unsafe_allow_html=True,
)

# 1. Fetch the API key securely from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Missing Gemini API Key! Please add 'GEMINI_API_KEY' to your Streamlit App Secrets.")
    st.stop()

# 2. Initialize the Gemini Client and Chat session securely in Session State
if "robo" not in st.session_state:
    st.session_state.robo = genai.Client(api_key=api_key)

if "mychat" not in st.session_state:
    st.session_state.mychat = st.session_state.robo.chats.create(model="gemini-2.5-flash")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

send = st.button("Send")

# 3. Handle message execution securely
if send and question:
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.mychat.send_message(question)
            response_placeholder.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
