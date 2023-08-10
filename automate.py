import pyautogui
import keyboard
from time import sleep


actions_list = []


def startRecording():
    pass


if __name__ == "__main__":
    print("Listening started\nPress c to register a click\nPress i to record mouse position")
    while True:
        if keyboard.is_pressed("c"):
            print("Recorded a click")
            actions_list.append("//click")
            sleep(1)
        if keyboard.is_pressed("i"):
            print("Recorded mouse position")
            x, y = pyautogui.position()
            actions_list.append((x, y))
            sleep(1)
        if keyboard.is_pressed("t"):
            custom_text = input(
                "Enter the text you want to type and press enter to register: ")
            actions_list.append(custom_text)
        if keyboard.is_pressed('esc'):
            print("Exiting recording session")
            break
    input("Press enter to start actions after 5 seconds")
    sleep(5)
    for action in actions_list:
        if type(action) == tuple:
            pyautogui.moveTo(action[0], action[1], 0.5,
                             pyautogui.easeInOutQuad)
        elif action == "//click":
            pyautogui.click()
        else:
            pyautogui.write(action, interval=0.1)
        sleep(1)
