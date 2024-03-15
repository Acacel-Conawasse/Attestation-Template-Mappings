import pyautogui
import time

def perform_actions(action):
    if action.startswith("Mouse Click"):
        # Extracting coordinates from the action string
        _, x, y = action.split()
        x, y = int(x), int(y)
        pyautogui.click(x, y)
    elif action == "Write Line Data":
        # Placeholder for writing line data, you need to implement this part
        print("Writing Line Data")
    elif action == "Key Press 2 Tabs":
        pyautogui.press('tab', presses=2)
    elif action == "Key Press enter":
        pyautogui.press('enter')

# Reading actions from DeleteInput.txt
with open("DeleteInput.txt", "r") as file:
    actions = file.readlines()

# Performing actions
for action in actions:
    action = action.strip()  # Removing leading/trailing whitespaces
    perform_actions(action)
    time.sleep(1)  # Adding a delay to allow time for actions to complete
