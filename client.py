import cohere
from cohere import ChatMessage

# Initialize Cohere client with your API key
co = cohere.Client("Rekn3oTSmRygRJWkWgYZqpeYelt58DcCiqEZUGSz")

import cohere
import re
from cohere import ChatMessage

def parse_whatsapp_chat_v2(raw_chat_text: str, chatbot_name: str) -> tuple[list[ChatMessage], str]:
    """
    Parses raw WhatsApp chat text, strictly assigning 'CHATBOT' to Kshitij
    and 'USER' to the other person (Deevika, etc.).

    Args:
        raw_chat_text: The string copied from WhatsApp.
        chatbot_name: The name of the persona the model is playing (e.g., "Kshitij").

    Returns:
        A tuple: ([structured_history], new_user_message)
    """
    
    # Regex to capture the speaker name and message content
    CHAT_LINE_PATTERN = re.compile(r"^\[.*?\]\s*([^:]+?):\s*(.+)$", re.MULTILINE)
    
    matches = CHAT_LINE_PATTERN.findall(raw_chat_text.strip())
    
    if not matches:
        return [], "" # No matches found, no history or message
        
    structured_history = []
    
    # --- 1. Process Chat History (All lines EXCEPT the last one) ---
    # These messages set the context.
    for timestamped_message in matches[:-1]:
        speaker = timestamped_message[0].strip()
        message_text = timestamped_message[1].strip()
        
        # Determine the role based on the name comparison
        if speaker.lower() == chatbot_name.lower():
            role = "CHATBOT"
        else:
            # Anyone NOT the chatbot is the USER
            role = "USER" 
        
        structured_history.append(ChatMessage(role=role, message=message_text))

    # --- 2. Extract the NEW user message (the last line) ---
    # This is the prompt the model must respond to.
    last_speaker, new_prompt = matches[-1]
    
    # Crucial check: If the last message is from the chatbot (Kshitij), 
    # there is nothing new for the bot to reply to, so we return an empty prompt.
    if last_speaker.lower() == chatbot_name.lower():
        print(f"⚠️ Warning: The last message is from {chatbot_name}. No new message to respond to.")
        return structured_history, "" 

    # Since the last message is from the *other* person (USER), it becomes the prompt.
    print(f"✅ New User Prompt detected from {last_speaker}.")
    return structured_history, new_prompt.strip()

# --- EXAMPLE USAGE ---

# 1. Define the Chatbot's Identity
CHATBOT_NAME = "Kshitij"

# 2. Simulate Clipboard Content (The latest message is from Deevika, which Kshitij must answer)
raw_chat_text_from_clipboard = '''
[9:42 AM, 10/4/2025] Kshitij: Chlo bdia
[9:43 AM, 10/4/2025] Deevika: Hmm
[9:52 AM, 10/4/2025] Kshitij: Ji
[10:05 AM, 10/4/2025] Deevika: Tera next lecture kab hai?
'''
# NOTE: The last line is the NEW user message. All lines before it form the history.

# 3. Parse the text
structured_history, new_user_message = parse_whatsapp_chat_v2(
    raw_chat_text_from_clipboard, 
    CHATBOT_NAME
)

# 4. Final Output Check (Before sending to Cohere)
print(f"--- History Turns ---")
for msg in structured_history:
    print(f"Role: {msg.role} (Parsed Speaker: {CHATBOT_NAME if msg.role == 'CHATBOT' else 'Deevika/Other'}): {msg.message}")

print("---------------------")
print(f"New Prompt for Kshitij: {new_user_message}")