import pyautogui
import keyboard
import time
import random
import tkinter as tk
from tkinter import ttk
from threading import Thread

# Messages to be typed
messages = ["owo hunt", "owo battle"]

# Delay ranges
delay_hunt_min = 15  # Minimum delay for "owo hunt"
delay_hunt_max = 25  # Maximum delay for "owo hunt"
delay_battle_min = 1  # Minimum delay for "owo battle"
delay_battle_max = 5  # Maximum delay for "owo battle"

# Typing and sending messages
def type_message(message):
    pyautogui.typewrite(message)  # Type the message
    pyautogui.press('enter')      # Press Enter to send

# Countdown display function
def countdown(seconds, label):
    for i in range(seconds, 0, -1):
        label.config(text=f"Next message in {i} seconds")  # Update countdown label
        label.update()  # Update the UI
        time.sleep(1)  # Wait for 1 second
    label.config(text="Sending message...")  # Clear the label once the countdown is done

# Main function to send messages in a loop
def main(label):
    while True:
        if keyboard.is_pressed('ctrl+alt'):  # Stop the program if 'Ctrl+Alt' is pressed
            label.config(text="Program stopped.")
            break
        
        # Send "owo hunt"
        type_message(messages[0])
        
        # Random delay for "owo hunt"
        delay_hunt = random.randint(delay_hunt_min, delay_hunt_max)
        countdown(delay_hunt, label)
        
        # Send "owo battle"
        type_message(messages[1])
        
        # Random delay for "owo battle"
        delay_battle = random.randint(delay_battle_min, delay_battle_max)
        countdown(delay_battle, label)

# Thread to run the typing process
def start_typing_process(label):
    # Wait until user presses the hotkey 'Ctrl+Shift' to start
    label.config(text="Focus on the textbox and press 'Ctrl+Shift' to start.")
    keyboard.wait('ctrl+shift')
    
    # Run the typing loop in a new thread
    thread = Thread(target=lambda: main(label))
    thread.daemon = True
    thread.start()

# Function to handle the start button in a separate thread
def start_button_pressed(label):
    # Run the keyboard listener in a separate thread to avoid blocking the UI
    thread = Thread(target=lambda: start_typing_process(label))
    thread.daemon = True  # Daemon thread to stop with the program
    thread.start()

# Create modern UI using tkinter
def create_gui():
    root = tk.Tk()
    root.title("OwO Message Sender")
    root.geometry("400x200")
    root.resizable(False, False)
    
    # Make the window always on top
    root.attributes('-topmost', True)

    # Styling the UI with ttk for a modern look
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14), padding=10)
    style.configure("TLabel", font=("Arial", 12))

    # Start button
    start_button = ttk.Button(root, text="Start", command=lambda: start_button_pressed(countdown_label))
    start_button.pack(pady=20)

    # Countdown label to show the message timing
    countdown_label = ttk.Label(root, text="Waiting to start...")
    countdown_label.pack(pady=10)

    # Run the tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
