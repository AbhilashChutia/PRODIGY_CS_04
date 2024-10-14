from pynput.keyboard import Listener
import tkinter as tk
from tkinter import messagebox
import signal
import sys

# Path to save the log file
log_file = "keylog.txt"

# Function to log keystrokes
def log_key(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key.startswith('Key'):
        key = ''

    with open(log_file, "a") as f:
        f.write(key)

# Function to get user permission through UI
def get_user_permission():
    root = tk.Tk()
    root.withdraw()
    
    response = messagebox.askyesno("Permission Request", "This script will log your keystrokes. Do you give permission to proceed?")
    
    if response:
        messagebox.showinfo("Permission Granted", "Starting keylogger...")
        return True
    else:
        messagebox.showinfo("Permission Denied", "Exiting script.")
        root.quit()
        return False

# Signal handler for Ctrl+C
def signal_handler(sig, frame):
    print("\nScript terminated by user (Ctrl+C). Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Check for permission before starting
    if get_user_permission():
        try:
            # Start key logging
            with Listener(on_press=log_key) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("\nScript terminated by user (Ctrl+C). Exiting...")
            sys.exit(0)
