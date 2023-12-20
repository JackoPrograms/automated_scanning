powershell.exe -ExecutionPolicy Bypass -File start_Windows.ps1

@echo off
cd /d %~dp0
start "" python server.py
timeout /t 2
start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"