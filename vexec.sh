#!/bin/bash

cd "$(dirname "$0")"

if [ "$1" == "--key" ]; then
    python3 ./src/main.py "$@"
elif [ "$1" == "--admin" ]; then
    all_args="$*"
    args="${all_args:8}"
    x-terminal-emulator -e "/bin/bash -c \"./vexec.sh $args\""
else
    python3 ./src/main.py "$@"
fi