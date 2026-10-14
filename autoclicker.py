import time
import threading
import pyautogui
import keyboard


TOGGLE_KEY = 'f6'   
EXIT_KEY = 'f7'     
CLICK_DELAY = 0.001


clicking = False

def clicker():
    """Function that continuously clicks when the toggle is active."""
    global clicking
    print(f"[*] Autoclicker thread started. Use [{TOGGLE_KEY}] to toggle.")
    
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(CLICK_DELAY)
        else:
            time.sleep(0.1) 

def toggle_clicking():
    """Toggles the clicking state on and off."""
    global clicking
    clicking = not clicking
    if clicking:
        print("[+] Autoclicker: STARTED")
    else:
        print("[-] Autoclicker: STOPPED")

def main():
    click_thread = threading.Thread(target=clicker, daemon=True)
    click_thread.start()

    keyboard.add_hotkey(TOGGLE_KEY, toggle_clicking)
    
    print("=========================================")
    print(f" Autoclicker active! Press [{TOGGLE_KEY}] to Start/Stop.")
    print(f" Press [{EXIT_KEY}] to exit the program safely.")
    print("=========================================")

    keyboard.wait(EXIT_KEY)
    print("[!] Exiting autoclicker. Goodbye!")

if __name__ == "__main__":
    main()
