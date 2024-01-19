#!/bin/bash

cd "$(dirname "$0")"

if [ "$1" == "--key" ]; then
    python ./src/main.py "$@"
elif [ "$1" == "--ueli" ]; then
    all_args="$*"
    args="${all_args:7}"
    x-terminal-emulator -e "/bin/bash -c \"./vexec.sh $args\""
else
    python ./src/main.py "$@"
fi