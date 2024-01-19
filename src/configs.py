import json

def load_text_config(path):
    with open("./configs/" + path, 'r') as f:
        return f.read()

def load_json_config(path):
    with open("./configs/" + path, 'r') as f:
        return json.load(f)

def save_json_config(path, data):
    with open("./configs/" + path, 'w') as f:
        json.dump(data, f)

try:
    OPENAI_CONFIG = load_json_config('config.json')
except FileNotFoundError:
    OPENAI_CONFIG = { "apikey": None }