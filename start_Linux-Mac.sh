#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$DIR/server.py" &
sleep 2
"./Mozilla Firefox/firefox.exe" "http://127.0.0.1:5000"