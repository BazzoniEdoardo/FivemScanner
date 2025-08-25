# FiveM Scanner Tool

A simple Python tool to gather detailed information about **FiveM servers**, including players, resources, server variables, and general server info.

---

## Features

- Fetches server information via the official FiveM API.
- Saves results into separate JSON files:
  - **RawData.json** – raw server data
  - **PlayerListData.json** – list of players
  - **ResourceListData.json** – list of resources
  - **ServerInfoData.json** – general server information
  - **VarsData.json** – server variables
- Simple text-based interface with ASCII logo and success/error messages.

---

## Requirements

- Python 3.10+  
- Python libraries:
  - `playwright`

---

## Installation

There are three ways to install dependencies and set up the tool:

1. **Using the provided build script**  
   - Windows: `build.bat`  
   - Linux/macOS: `build.sh`  
   These scripts will install the required Python packages and set up Playwright browsers.

2. **Using `requirements.txt`**  
   ```bash
   pip install -r requirements.txt
   python -m playwright install
   ```

---

## Usage

Run the tool with the server ID as an argument:

```bash
python fivemscanner.py <server_id>
```

Example:

```bash
python fivemscanner.py abc123
```

### What happens:
- It fetches all data from the server with the given ID.
- It creates a folder in `results/<server_id>/`.

- It saves multiple JSON files containing server information.
