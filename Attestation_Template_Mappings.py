import pyautogui
import time

def automate_process(file_path):
    with open(file_path, 'r') as file, open('log.txt', 'a') as log_file:
        next(file)  # Skip the header row
        for line in file:
            columns = line.strip().split(',')
            time.sleep(0.5)
            
            # Assuming specific coordinates for clicks and button presses are known
            # Replace 'x_click', 'y_click', etc., with actual coordinates or button names

            # Click the Location X template
            pyautogui.click(1118, 268)
            time.sleep(0.5) 
            # Click on the copy icon
            pyautogui.click(1798, 190)
            time.sleep(0.5)
            # Initial position click
            pyautogui.click(1252, 131)
            time.sleep(0.5)
            # Press tab 3 times
            pyautogui.press('tab', presses=3, interval=0.25)
            time.sleep(0.5)
            # Enter data from col 0
            pyautogui.write(columns[0])
            time.sleep(0.5)
            # Press tab 3 times
            pyautogui.press('tab', presses=3, interval=0.25)
            time.sleep(0.5)
            # Press Ctrl+A then Backspace
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.press('backspace')
            time.sleep(0.5)
            # Enter data from col 1
            pyautogui.write(columns[1])
            time.sleep(0.05)
            # Press tab 9 times
            pyautogui.press('tab', presses=9, interval=0.25)
            time.sleep(0.05)
            # Click edit position
            pyautogui.click(1838, 646)
            time.sleep(0.75)
            # Press tab 3 times
            pyautogui.press('tab', presses=3, interval=0.25)
            time.sleep(0.7)
            # Press Ctrl+A then Backspace
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.7)
            pyautogui.press('backspace')
            time.sleep(0.7)
            # Enter data from col 2
            pyautogui.write(columns[2])
            time.sleep(0.7)
            # Press tab once
            pyautogui.press('tab')
            time.sleep(0.7)
            # Press enter
            pyautogui.press('enter')
            time.sleep(0.7)
            #Save
            pyautogui.click(1892, 206)
            time.sleep(0.7)
            
            time.sleep(2)
            pyautogui.click(1885,158)
            time.sleep(0.05)
            pyautogui.click(1905,162)

            log_file.write(f"Successfully created {columns[0]}\n")
            time.sleep(1)  # Add delay as needed for UI to respond

# Replace 'x_base', 'y_base', etc., with actual coordinates or actions
automate_process('Automate_Template_Data.txt')

"""
Input Example: 
ATKName, Discription, CostCenter
XnameSample, XnameSample Disc, 48012548864
XnameSample1, XnameSample Disc, 480125488641
XnameSample2, XnameSample Disc, 48012548864
"""