#!/bin/bash

set -e

echo "=== Начало процесса CI ==="

git pull origin master
pip install -r requirements.txt
python -m unittest operations_tests.py
python -m unittest main_class_tests.py

# Сборка исполняемого файла через PyInstaller
pyinstaller --onefile main.py

echo "=== Процесс CI успешно завершен ==="
