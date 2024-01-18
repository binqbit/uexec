# uexec - ueli tool to execute command with text converted from speech
This tool is useful for teams that use AI to process text information to perform necessary actions, for example gpt in the terminal.

## Installation
```shell
pip install -r requirements.txt
```

## Set api key
```shell
uexec --key <api_key>
```

## How to use as custom command in ueli
- Open ueli settings
- Go to shortcuts
- Add new shortcut
Name: set command name (for example gpt)
Command:
```shell
aexec gpt
aexec gpt {{query}} --key <api_key>
```