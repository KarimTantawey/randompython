import time
import pyautogui
import keyboard

stop = False

def capture_screenshot():
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
    screenshot = pyautogui.screenshot()
    filename = f'screenshot{timestamp}.png'
    screenshot.save(filename)
    print(f'Screenshot saved: {filename}')

def on_keypress(event):
    global stop
    if event.name == 'u' and keyboard.is_pressed('ctrl'):
        stop = True
        print('Script stopped.')
keyboard.on_press(on_keypress)

interval = 5
while not stop:
    capture_screenshot()
    time.sleep(interval)
keyboard.unhook_all()


