import sys
from google import genai
import streamlit as st

# 1. Custom CSS injection for the Send button
st.markdown(
    """
    <style>
    /* target the button container to center it */
    div.stButton {
        text-align: center;
    }
    
    /* Style the actual button element */
    div.stButton > button {
        background-color: #4CAF50; /* Modern green color */
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

    /* Hover effect */
    div.stButton > button:hover {
        background-color: #45a049 !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    /* Click / Active effect */
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

# Initialize the Gemini Client
robo = genai.Client(
    api_key="MY_API"
)
mychat = robo.chats.create(model="gemini-2.5-flash")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

# Centered button using the CSS rule above
send = st.button("Send")

if send and question:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)
