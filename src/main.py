import os
from configs import OPENAI_CONFIG, save_json_config
from openai_models.whisper import translate_audio
from tools.console import print_one_line
from tools.speech import listen_and_save
import platform


def is_windows():
    return platform.system().lower() == 'windows'
    
def listen_message():
    if is_windows():
        import winsound
        winsound.Beep(1000, 300)
    print("listening...")
    listen_and_save(f"./data/voice.wav", True)
    audio_file = open("./data/voice.wav", "rb")
    return translate_audio(audio_file)



def main():
    args = os.sys.argv
    if args[1] == "--key":
        OPENAI_CONFIG["api_key"] = args[2]
        save_json_config("config.json", OPENAI_CONFIG)
        return
    
    if not OPENAI_CONFIG["api_key"]:
        print("No API key found. Please use --key to set your API key.")
        os.system("pause")
        return
    
    if args[1] == "--minimize":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        skip = 2
    else:
        skip = 1
    
    query = ' '.join(args[skip:])
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