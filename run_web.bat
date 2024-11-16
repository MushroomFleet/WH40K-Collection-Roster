@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Army Manager Web Interface (Local Only)...
echo The interface will open in your default browser
echo Only connections from this computer will be allowed
echo.
python gradio_interface.py

echo Deactivating virtual environment...
deactivate
pause