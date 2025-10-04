# modules/translator.py

from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")

def translate_to_english(text):
    try:
        result = translator(text)
        return result[0]["translation_text"]
    except Exception as e:
        return f"Translation error: {e}"
