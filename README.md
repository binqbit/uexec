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
vexec --admin ...
vexec --admin --minimize ... - minimize terminal window after command execution
```

## How to use as custom command in ueli
- Open ueli settings
- Go to shortcuts
- Add new shortcut
- Name: command name (for example gpt)
- Command:
```shell
vexec --admin gpt
vexec --admin gpt {{query}} --key <api_key>
```

## How to use as hotkey
- Create new bat file with your command and flag --admin
- Create shortcut for this bat file
- Open shortcut properties
- Set hotkey
- Example:
```shell
vexec --admin ask-gpt
```