import mouse
import keyboard
import time
import matplotlib.pyplot as plt


def main():
    mouse_minute_data = {}
    keyboard_minute_data = {}
    mins = int(input('How many minutes would you like to analyze? '))
    print()
    i = 0
    while i < mins:
        mouse_events = []

        mouse.hook(mouse_events.append)
        keyboard.start_recording()

        time.sleep(60)

        mouse.unhook(mouse_events.append)
        keyboard_events = keyboard.stop_recording()

        mouse_minute_data[i + 1] = len(mouse_events)
        keyboard_minute_data[i + 1] = len(keyboard_events)

        i += 1

    for (mouse_minute, mouse_data), (keyboard_minute, keyboard_data) in zip(mouse_minute_data.items(),
                                                                            keyboard_minute_data.items()):
        print('Minute ', mouse_minute, ':')
        print(mouse_data, 'mouse events')
        print(keyboard_data, 'keyboard events')
        print()

    plt.plot(mouse_minute_data.keys(), mouse_minute_data.values(), color='red', label='Mouse Events')
    plt.plot(keyboard_minute_data.keys(), keyboard_minute_data.values(), color='blue', label='Keyboard Events')
    plt.title('Productivity Analysis')
    plt.xlabel('Minutes')
    plt.ylabel('Events per minute')
    plt.legend()
    plt.show()
