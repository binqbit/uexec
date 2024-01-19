from configs import OPENAI_CONFIG
import openai



openai.api_key = OPENAI_CONFIG['api_key']

def translate_audio(audio_file):
    transcript = openai.Audio.translate("whisper-1", audio_file)
    text = transcript["text"].strip()
    if text.isspace():
        text = ""
    return text