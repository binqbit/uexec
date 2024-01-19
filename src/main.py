
import json
import os
from configs import OPENAI_CONFIG, save_json_config
from openai_models.whisper import translate_audio
from tools.console import print_one_line
from tools.speech import listen_and_save
import winsound



def listen_message():
    winsound.Beep(1000, 300)
    print("listening...")
    listen_and_save(f"./data/voice.wav", True)
    audio_file = open("./data/voice.wav", "rb")
    return translate_audio(audio_file)



def main():
    args = os.sys.argv
    if args[1] == "--key":
        OPENAI_CONFIG["apikey"] = args[2]
        save_json_config("config.json", OPENAI_CONFIG)
        return
    
    if not OPENAI_CONFIG["apikey"]:
        print("No API key found. Please use --key to set your API key.")
        os.system("pause")
        return
    
    query = ' '.join(args[1:])
    msg = listen_message()
    
    if "{{query}}" in query:
        cmd = query.replace("{{query}}", msg)
    else:
        cmd = query + " " + msg

    print("> " + cmd)
    print_one_line()
    os.system(cmd)

if __name__ == "__main__":
    main()