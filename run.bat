@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Army Manager...
python main.py

echo Deactivating virtual environment...
deactivate
pause
