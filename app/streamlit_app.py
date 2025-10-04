import sys
import os
import tempfile
import streamlit as st

# Ensure module path is available
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module.chatbot_core import get_response

from module.tesseract_input import extract_text_from_image
from module.whisper_input import transcribe_audio
from module.translator import translate_to_english

st.title("🩺 Public Health Chatbot")

# 💬 Text input
user_input = st.text_input("Ask a health question :")
if user_input:
    try:
        response = get_response(user_input)
        st.write("🤖", response)
    except Exception as e:
        st.error(f"Error: {e}")

# 🖼️ Image upload
uploaded_image = st.file_uploader("Upload a health image", type=["png", "jpg", "jpeg"])
if uploaded_image:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(uploaded_image.getbuffer())
        extracted_text = extract_text_from_image(tmp.name)
    st.write("📝 Extracted Text:")
    st.text(extracted_text)

# 🎤 Audio upload
st.header("🎤 Voice Input")
uploaded_audio = st.file_uploader("Upload an audio question", type=["wav", "mp3"])
if uploaded_audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_audio.getbuffer())
        transcribed_text = transcribe_audio(tmp.name)
    st.write("🗣️ Transcribed Text:")
    st.text(transcribed_text)
    response = get_response(transcribed_text)
    st.write("🤖", response)

# 🌍 Multilingual
st.header("🌍 Multilingual Support")
foreign_input = st.text_input("Enter a health question in another language:")
if foreign_input:
    translated = translate_to_english(foreign_input)
    st.write("🔄 Translated to English:")
    st.text(translated)
    response = get_response(translated)
    st.write("🤖", response)









