@echo off
REM --- Build script for Windows ---

echo Building FiveM Scanner Tool...

REM Check Python installation
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python not found! Make sure to have python installed!.
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install playwright

REM Install Playwright browsers
python -m playwright install

echo Build completed successfully!
pause