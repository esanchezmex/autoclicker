#!/usr/bin/env python3
import time
import subprocess
import pyautogui  # You'll need to install this with: pip3 install pyautogui

# Disable pyautogui's fail-safe (optional)
# This prevents the program from stopping if you move your mouse to a corner
pyautogui.FAILSAFE = False

def get_screen_size():
    """Get the screen resolution of the primary display."""
    screen_width, screen_height = pyautogui.size()
    return screen_width, screen_height

def click_middle():
    """Click three times in the middle of the screen with 2-second intervals."""
    screen_width, screen_height = get_screen_size()
    middle_x = screen_width // 2
    middle_y = screen_height // 2
    
    print(f"Clicking at position ({middle_x}, {middle_y})")
    
    # First click
    pyautogui.click(middle_x, middle_y)
    print("Click 1")
    
    # Wait 2 seconds
    time.sleep(2)
    
    # Second click
    pyautogui.click(middle_x, middle_y)
    print("Click 2")
    
    # Wait 2 seconds
    time.sleep(2)
    
    # Third click
    pyautogui.click(middle_x, middle_y)
    print("Click 3")
    
    print("Waiting 5 minutes until next set of clicks...")

def main():
    print("Auto-clicker started. Press Ctrl+C to stop.")
    print("This script will click in the middle of your screen three times (2 seconds apart) every 5 minutes.")
    print("Your computer will be prevented from sleeping while this script runs.")
    
    # Start caffeinate in a subprocess to prevent sleep
    # -d prevents display sleep, -i prevents system idle sleep
    caffeinate_process = subprocess.Popen(["caffeinate", "-d", "-i"])
    
    try:
        while True:
            click_middle()
            # Wait for 5 minutes (300 seconds) before the next set of clicks
            # We already waited 4 seconds during the clicking, so we wait 296 more
            time.sleep(296)
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")
        # Kill the caffeinate process when the script stops
        caffeinate_process.terminate()

if __name__ == "__main__":
    main()
