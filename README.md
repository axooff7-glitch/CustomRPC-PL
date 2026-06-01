```markdown
# Discord Custom RPC App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</p>

Desktop application for creating and managing custom Discord Rich Presence easily through a graphical interface.

---

## Overview

Discord Custom RPC App allows you to set your own Rich Presence without modifying code.  
Simply enter your Application ID and activity details, then start the RPC with one click.

Built with:
- Python
- Tkinter (GUI)
- pypresence (Discord RPC)

---

## Features

- Custom details and state text
- Large and small image support
- Image tooltip text support
- Start / Stop RPC button
- Clean and simple interface
- Lightweight and fast

---

## Requirements

- Python 3.10+
- Discord Desktop App running
- Internet connection

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/discord-custom-rpc.git
cd discord-custom-rpc
```

### 2. Install dependencies

```bash
py -m pip install pypresence
```

or

```bash
python -m pip install pypresence
```

---

## Setup (Discord Developer Portal)

1. Go to:  
   https://discord.com/developers/applications

2. Click **New Application**
3. Copy your **Application ID**
4. Go to **Rich Presence → Art Assets**
5. Upload your images (example: `logo`)
6. Save changes

---

## Usage

Run the application:

```bash
python custom_rpc_app.py
```

Fill in:
- Client ID
- Details (top text)
- State (bottom text)
- Image names (must match uploaded assets)

Click **START RPC**

Make sure Discord is open.

---

## Project Structure

```
discord-custom-rpc/
│
├── custom_rpc_app.py
├── README.md
└── requirements.txt (optional)
```

---

## Build to EXE (Optional)

You can convert the app to an executable:

```bash
py -m pip install pyinstaller
py -m pyinstaller --onefile --windowed custom_rpc_app.py
```

The executable will be located in:

```
dist/
```

---

## Troubleshooting

If installation fails:

```bash
py -m pip install --upgrade pip
```

If RPC does not appear:
- Make sure Discord is running
- Verify correct Application ID
- Ensure image names match exactly

---

## License

MIT License
```
