@echo off
cd /d %~dp0
py -m pip install docker
start "" python server.py
timeout /t 2
start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"