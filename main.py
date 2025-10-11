import pyautogui
import pyperclip
import time
import cohere
import re
from cohere import ChatMessage
import os

# --- CONFIGURATION (Defined once for efficiency) ---
# NOTE: It is highly recommended to use environment variables for keys.
co = cohere.Client("Rekn3oTSmRygRJWkWgYZqpeYelt58DcCiqEZUGSz")

CHATBOT_NAME = "Kshitij"
PREAMBLE = "You are Kshitij, a Hindi-English speaking BCA student from GGDSD College, Sector-32. Respond like him. Keep your answers concise and casual, like a friend chatting on WhatsApp."


# --- INACTIVITY BREAK CONFIGURATION ---
BREAK_MESSAGE_INTERVAL = 60  # seconds (1 minute)
BREAK_MESSAGE_TEXT = "Chalo, kya scene hai? Bored ho gya, kuch bol." # Casual break message
LAST_REPLY_TIME = time.time() # Track the last time Kshitij sent a message (either a reply or a break message)


# --- PARSING FUNCTION (Defined once outside the loop) ---
def parse_whatsapp_chat_v2(raw_chat_text: str, chatbot_name: str) -> tuple[list[ChatMessage], str]:
    """
    Parses raw WhatsApp chat text, strictly assigning 'CHATBOT' to Kshitij
    and 'USER' to the other person (Deevika, etc.).
    """
    
    # Regex to capture the speaker name and message content
    CHAT_LINE_PATTERN = re.compile(r"^\[.*?\]\s*([^:]+?):\s*(.+)$", re.MULTILINE)
    
    matches = CHAT_LINE_PATTERN.findall(raw_chat_text.strip())
    
    if not matches:
        return [], "" 
        
    structured_history = []
    
    # Process Chat History (All lines EXCEPT the last one)
    for timestamped_message in matches[:-1]:
        speaker = timestamped_message[0].strip()
        message_text = timestamped_message[1].strip()
        
        if speaker.lower() == chatbot_name.lower():
            role = "CHATBOT"
        else:
            role = "USER" 
        
        structured_history.append(ChatMessage(role=role, message=message_text))

    # Extract the NEW user message (the last line)
    last_speaker, new_prompt = matches[-1]
    
    # Crucial check: If the last message is from the chatbot (Kshitij), 
    # there is nothing new for the bot to reply to.
    if last_speaker.lower() == chatbot_name.lower():
        print(f"⚠️ Warning: Last message is from {chatbot_name}. Skipping reply.")
        return structured_history, "" 

    return structured_history, new_prompt.strip()

# --- INITIAL SETUP ---

# Give yourself a moment to focus on the window before the loop starts
print("Starting WhatsApp Auto-Responder. Press Ctrl+C to stop.")
# This initial click focuses the WhatsApp window before monitoring begins.
pyautogui.click(1293, 1053) 
time.sleep(1)


# --- MAIN AUTOMATION LOOP ---
while True:
    try:
        # 1. Skip the redundant focus click here, as the initial click should suffice.
        time.sleep(0.5)

        # 2. Drag to select the text
        pyautogui.moveTo(672, 230)
        pyautogui.dragTo(789, 947, duration=0.2, button='left') 
        time.sleep(0.1)

        # 3. Copy the selected text (Ctrl+C)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)

        # 4. Retrieve copied text from clipboard
        chat_history = pyperclip.paste()

        # 5. Parse the raw text
        structured_history, new_user_message = parse_whatsapp_chat_v2(
            chat_history, 
            CHATBOT_NAME
        )
        
        # 6. Call Cohere API and Automate Reply
        if new_user_message:
            # --- Scenario 1: User sent a NEW message (Normal Reply) ---
            try:
                response = co.chat(
                    model="command-r-plus-08-2024", 
                    preamble=PREAMBLE,
                    chat_history=structured_history,
                    message=new_user_message
                )
                
                ai_reply = response.text.strip()
                
                # --- AUTOMATION: PASTE AND SEND ---
                pyperclip.copy(ai_reply)
                
                pyautogui.click(1125, 960)
                time.sleep(0.5)

                pyautogui.hotkey('ctrl','v')
                time.sleep(0.5)

                pyautogui.press('enter')
                
                # Update last reply time immediately after sending
                LAST_REPLY_TIME = time.time()

                # --- FINAL OUTPUT ---
                print("\n==================================")
                print("💡 AUTOMATED REPLY SENT (Kshitij):")
                print(ai_reply)
                print("==================================")
                
                time.sleep(20) # Wait longer after sending a reply

            except cohere.errors.UnauthorizedError:
                print("\n❌ AUTH ERROR: Please check your Cohere API key (401 error).")
                time.sleep(60) 
            except Exception as e:
                print(f"\n❌ An API Error occurred: {e}")
                time.sleep(20)

        else:
            # --- Scenario 2: No new message (Check for Inactivity Break) ---
            
            elapsed_time = time.time() - LAST_REPLY_TIME
            
            if elapsed_time > BREAK_MESSAGE_INTERVAL:
                print(f"⏰ Inactivity detected: Sending break message after {int(elapsed_time)}s.")
                
                # --- AUTOMATION: PASTE AND SEND BREAK MESSAGE ---
                break_message = BREAK_MESSAGE_TEXT
                pyperclip.copy(break_message)
                
                # Click the message input box (1125, 960)
                pyautogui.click(1125, 960)
                time.sleep(0.5)

                pyautogui.hotkey('ctrl','v')
                time.sleep(0.5)

                pyautogui.press('enter')
                
                # Update last reply time immediately after sending break message
                LAST_REPLY_TIME = time.time()
                
                # --- FINAL OUTPUT ---
                print(f"==================================")
                print(f"💬 BREAK MESSAGE SENT: {break_message}")
                print(f"==================================")
                time.sleep(20) # Wait a long time after sending an active message
            
            else:
                # No new message, and break interval hasn't been met yet
                time.sleep(10) 

    except KeyboardInterrupt:
        print("\nAuto-responder stopped by user.")
        break 
    except Exception as e:
        print(f"\n❌ PyAutoGUI/Clipboard Error in loop: {e}. Waiting 15s.")
        time.sleep(15)

