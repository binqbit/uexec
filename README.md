# vexec - tool to execute command with text converted from speech
This tool is useful for teams that use AI to process text information to perform necessary actions, for example gpt in the terminal.

## Installation
```shell
pip install -r requirements.txt
```

## Set api key
```shell
vexec --key <api_key>
```

## How to use
```shell
vexec <command>
vexec {{query}} <command>
vexec --ueli ...
```

## How to use as custom command in ueli
- Open ueli settings
- Go to shortcuts
- Add new shortcut
- Name: command name (for example gpt)
- Command:
```shell
vexec --ueli gpt
vexec --ueli gpt {{query}} --key <api_key>
```
