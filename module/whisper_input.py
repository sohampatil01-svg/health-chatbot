# modules/whisper_input.py

import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"Error transcribing audio: {e}"
