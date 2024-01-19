from configs import OPENAI_CONFIG
import openai



openai.apikey = OPENAI_CONFIG['apikey']

def translate_audio(audio_file):
    transcript = openai.Audio.translate("whisper-1", audio_file)
    text = transcript["text"].strip()
    if text.isspace():
        text = ""
    return text