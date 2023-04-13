from pynput import keyboard

def on_press(key):
    print('se presiono la tecla: ',str(key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
