from pynput import keyboard
import time

start = time.time()

def on_release(key):
    with open(f"data.txt", "a") as file:
        current = time.time() - start
        key = str(key).split('.')[-1]
        file.write(f"{key}, {round(current, 3)}\n")

    print('{0} released'.format(key))

with keyboard.Listener(on_release=on_release) as Listener:
    Listener.join()