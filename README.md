# AI Auto-Reply Chat Bot

> Automate WhatsApp replies using Python and Cohere AI with a personalized touch.

---

## Overview

**AI Auto-Reply Chat Bot** is a Python-based automation project that automatically reads WhatsApp chat messages and responds intelligently using **Cohere's Command-R Plus model**.

The bot, named **Kshitij**, is designed to mimic your chat style, respond fluently in both **Hindi and English**, and can send casual "break messages" during periods of inactivity. This project was built to enhance my Python skills and explore the practical integration of desktop automation and generative AI.

---

## Features

- **Real-Time Parsing:** Parses WhatsApp chat messages in real-time.
- **Context-Aware AI:** Generates context-aware, human-like replies using Cohere's `command-r-plus` model.
- **Automated Sending:** Sends automated replies directly within the WhatsApp interface.
- **Break Message Feature:** Sends a casual message after a set interval of inactivity.
- **Customizable:** Fully customizable screen coordinates for different chat window positions.
- **Logging:** Logs all automated replies and activity in the console for monitoring.

---

## Tech Stack

| Component | Library/Version | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.13.5 | Core development language. |
| **AI Model** | `cohere` | Generative AI chat generation (`command-r-plus`). |
| **Automation** | `pyautogui` | Desktop automation (click, drag, type). |
| **Clipboard** | `pyperclip` | Handling clipboard data for chat history. |
| **Parsing** | `re` | Regex-based chat message parsing. |
| **Timing** | `time` | Managing timing and automation loops. |
| **Platform** | Windows | Primary development and testing environment. |

---

## Setup Instructions

### 1. Clone and Setup

```bash
# Clone the repository
git clone [https://github.com/kshitij-gamedev-007/Ai-Auto-Reply-Chat-Bot.git](https://github.com/kshitij-gamedev-007/Ai-Auto-Reply-Chat-Bot.git)
cd Ai-Auto-Reply-Chat-Bot

# Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

2. Set API Key
    Set your Cohere API key as an environment variable (recommended):
        $env:COHERE_API_KEY="YOUR_COHERE_API_KEY"
Alternatively, you can replace the key directly in client.py (not recommended for production).

I see you want the entire README file as a single, ready-to-use block.

Here is the complete Markdown text for your GitHub README:

Markdown

# AI Auto-Reply Chat Bot

> Automate WhatsApp replies using Python and Cohere AI with a personalized touch.

---

## Overview

**AI Auto-Reply Chat Bot** is a Python-based automation project that automatically reads WhatsApp chat messages and responds intelligently using **Cohere's Command-R Plus model**.

The bot, named **Kshitij**, is designed to mimic your chat style, respond fluently in both **Hindi and English**, and can send casual "break messages" during periods of inactivity. This project was built to enhance my Python skills and explore the practical integration of desktop automation and generative AI.

---

## Features

- **Real-Time Parsing:** Parses WhatsApp chat messages in real-time.
- **Context-Aware AI:** Generates context-aware, human-like replies using Cohere's `command-r-plus` model.
- **Automated Sending:** Sends automated replies directly within the WhatsApp interface.
- **Break Message Feature:** Sends a casual message after a set interval of inactivity.
- **Customizable:** Fully customizable screen coordinates for different chat window positions.
- **Logging:** Logs all automated replies and activity in the console for monitoring.

---

## Tech Stack

| Component | Library/Version | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.13.5 | Core development language. |
| **AI Model** | `cohere` | Generative AI chat generation (`command-r-plus`). |
| **Automation** | `pyautogui` | Desktop automation (click, drag, type). |
| **Clipboard** | `pyperclip` | Handling clipboard data for chat history. |
| **Parsing** | `re` | Regex-based chat message parsing. |
| **Timing** | `time` | Managing timing and automation loops. |
| **Platform** | Windows | Primary development and testing environment. |

---

## Setup Instructions

### 1. Clone and Setup

```bash
# Clone the repository
git clone [https://github.com/kshitij-gamedev-007/Ai-Auto-Reply-Chat-Bot.git](https://github.com/kshitij-gamedev-007/Ai-Auto-Reply-Chat-Bot.git)
cd Ai-Auto-Reply-Chat-Bot

# Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
2. Set API Key
Set your Cohere API key as an environment variable (recommended):

PowerShell

$env:COHERE_API_KEY="YOUR_COHERE_API_KEY"
Alternatively, you can replace the key directly in client.py (not recommended for production).

Usage
Preparation: Open WhatsApp Web and position the chat window properly on your screen.

Run the Bot:


python client.py


⚠️ Important Note
The bot relies heavily on hard-coded screen coordinates for desktop automation (pyautogui.click, dragTo). You must adjust these positions in the client.py file to match the layout of your WhatsApp window before running the bot.

Code Flow Summary
Focuses the WhatsApp window and selects the chat text.

Copies the chat history to the clipboard using pyperclip.

Parses new user messages from the chat history using regex (re).

Sends the new messages to the Cohere Chat API (command-r-plus-08-2024).

Receives the AI-generated reply and uses pyautogui to paste and send it into WhatsApp automatically.

Sends break messages after inactivity intervals.

Logs all activity in the console for easy monitoring.

Future Improvements
Multi-Platform Support: Extend functionality to platforms like Telegram and Discord.

GUI Implementation: Add a graphical user interface for easier setup, configuration, and monitoring.

Dynamic Detection: Implement dynamic detection of chat windows to eliminate the need for hard-coded coordinates.

Enhanced Personalization: Provide deeper AI personality customization for different contacts or groups.

License
This project is open-source and released under the MIT License.

Author
Kshitij (Pred4tor) – BCA Student