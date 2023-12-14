#!/bin/bash

# Задаем переменные для архива и папки назначения
ZIPFILE="./Mozilla Firefox/xul.zip"
DESTDIR="./Mozilla Firefox"

# Распаковываем архив в указанную папку без дополнительных подтверждений
unzip -o "$ZIPFILE" -d "$DESTDIR"

# # # Удаляем сам архив
rm './Mozilla Firefox/xul.zip'

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$DIR/server.py" &
sleep 2
"./Mozilla Firefox/firefox.exe" "http://127.0.0.1:5000"




# # Получаем полный путь к директории, где находится скрипт
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# # Запускаем сервер в новом окне терминала
# bash -- python3 "$DIR/server.py"

# # Даем серверу пару секунд на запуск
# sleep 2

# # Запускаем Firefox и открываем в нем локальный веб-сайт
# "./Mozilla Firefox/firefox.exe" "http://127.0.0.1:5000"