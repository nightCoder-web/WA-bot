import webbrowser
import time
import pyautogui
import urllib.parse

banner =  r'''
           _           _                                                                      _                 _   
          | |         | |                                                                    | |               | |
 __      _| |__   __ _| |_ ___  __ _ _ __  _ __    _ __ ___   ___  ___ ___  __ _  __ _  ___  | |__   ___   ___ | |__   ___ _ __ 
 \ \ /\ / / '_ \ / _` | __/ __|/ _` | '_ \| '_ \  | '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \ | '_ \ / _ \ / _ \| '_ \ / _ \ '__|
  \ V  V /| | | | (_| | |_\__ \ (_| | |_) | |_) | | | | | | |  __/\__ \__ \ (_| | (_| |  __/ | |_) | (_) | (_) | |_) |  __/ |   
   \_/\_/ |_| |_|\__,_|\__|___/\__,_| .__/| .__/  |_| |_| |_|\___||___/___/\__,_|\__, |\___| |_.__/ \___/ \___/|_.__/ \___|_|   
                                    |_|   |_|                                    |___/                                          '''

print(banner)

def whatsapp_message_boomer(phone_number, messages, delay):
    message_encoded = urllib.parse.quote(messages[0])
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message_encoded}"
    webbrowser.open(whatsapp_url)

    time.sleep(20)

    pyautogui.press("enter")

    try:
        for i, msg in enumerate(messages):
            time.sleep(delay)
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            print(f"Message {i + 1} sent: {msg}")
    except KeyboardInterrupt:
        print("\nStopped by user.")

def whatsapp_message_infinite(phone_number, message, delay):
    message_encoded = urllib.parse.quote(message)
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message_encoded}"
    webbrowser.open(whatsapp_url)

    time.sleep(20)
    pyautogui.press("enter")

    print("Started sending messages infinitely. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(delay)
            pyautogui.typewrite(message)
            pyautogui.press("enter")
    except KeyboardInterrupt:
        print("\nInfinite message sending stopped by user.")

print("Choose Mode:")
print("1. Send a specific number of messages")
print("2. Send messages infinitely (Press Ctrl+C to stop)")

choice = input("Enter your option (1 or 2): ")
phone_number = input("Enter the target WhatsApp number with country code (e.g., 91XXXXXXXXXX): ")

if choice == '1':
    print("Do you want to send different messages? (y/n)")
    different = input().lower()
    
    if different == 'y':
        count = int(input("How many different messages do you want to send? "))
        messages = []
        for i in range(count):
            msg = input(f"Enter message {i + 1}: ")
            messages.append(msg)
    else:
        msg = input("Enter the message: ")
        count = int(input("How many times to send it: "))
        messages = [msg] * count

    delay = int(input("Enter delay between messages (in seconds): "))
    whatsapp_message_boomer(phone_number, messages, delay)

elif choice == '2':
    msg = input("Enter a message to repeat infinitely: ")
    delay = int(input("Enter delay between messages (in seconds): "))
    whatsapp_message_infinite(phone_number, msg, delay)

else:
    print("Invalid option selected.")