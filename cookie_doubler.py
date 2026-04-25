import keyboard
import pyautogui
import time
import sys

# --- CONFIGURATION ---
# Time to wait (in seconds) for the browser console to open
CONSOLE_DELAY = 1.0  # Increased slightly for reliability

def double_cookies():
    """
    Function to double the current cookie count.
    It simulates opening the dev console, injecting the Game code, and closing it.
    """
    print("[ACTION] Doubling cookies...")
    
    # 1. Open the Browser Console (Ctrl+Shift+J forces the Console tab in Chrome/Edge)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(CONSOLE_DELAY)
    
    # 2. Type the Cookie Clicker internal command
    command = "Game.Earn(Game.cookies);"
    pyautogui.write(command, interval=0.01)
    pyautogui.press('enter')
    
    # 3. Close the Console
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    print("[SUCCESS] Cookies doubled. Grandmas are impressed.")

def shutdown_handler():
    """
    Cleanly exits the program.
    """
    print("\n[EXIT] Shutting down hotkey controller... Goodbye!")
    sys.exit(0)

def main():
    """
    Main loop that sets up listeners and keeps the script alive.
    """
    print("--- Cookie Clicker Hotkey Controller ---")
    print("Status: RUNNING")
    print("F6: Double Cookies (Make sure your browser is focused!)")
    print("F7: Exit Program")
    print("-----------------------------------------")

    # Hook the global hotkeys
    keyboard.add_hotkey('f6', double_cookies)
    keyboard.add_hotkey('f7', shutdown_handler)

    # Keep the main thread alive without hogging CPU
    try:
        keyboard.wait('f7')
    except KeyboardInterrupt:
        shutdown_handler()

if __name__ == "__main__":
    main()