#!/bin/bash
# Build script for Linux/macOS

echo "Building FiveM Scanner Tool..."

# Check Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found! Make sure to have Python installed."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install playwright

# Install Playwright browsers
python3 -m playwright install

echo "Build completed successfully!"