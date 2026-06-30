@echo off
cls
type logo.txt

pip install customtkinter
pip install cryptography
echo Python Libaries are installed.

if not exist key.key (python keyGen.py)

pause
