import pyautogui
import time

def automate_process(file_path):
    with open(file_path, 'r') as file, open('log.txt', 'a') as log_file:
        next(file)  # Skip the header row
        for line in file:
            columns = line.strip().split(',')
            time.sleep(0.07)
            
            # Assuming specific coordinates for clicks and button presses are known
            # Replace 'x_click', 'y_click', etc., with actual coordinates or button names

            # Click the Location X template
            pyautogui.click(x_base, y_base)
            time.sleep(0.07) 
            # Click on the copy icon
            pyautogui.click(copy, y_copy)
            time.sleep(0.07)
            # Initial position click
            pyautogui.click(x_initial, y_initial)
            time.sleep(0.07)
            # Press tab 3 times
            pyautogui.press('tab', presses=3, interval=0.25)
            time.sleep(0.07)
            # Enter data from col 0
            pyautogui.write(columns[0])
            time.sleep(0.07)
            # Press tab 2 times
            pyautogui.press('tab', presses=2, interval=0.25)
            time.sleep(0.07)
            # Press Ctrl+A then Backspace
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.07)
            pyautogui.press('backspace')
            time.sleep(0.07)
            # Enter data from col 1
            pyautogui.write(columns[1])
            time.sleep(0.07)
            # Press tab 9 times
            pyautogui.press('tab', presses=9, interval=0.25)
            time.sleep(0.07)
            # Click edit position
            pyautogui.click(x_edit, y_edit)
            time.sleep(0.07)
            # Press tab 3 times
            pyautogui.press('tab', presses=3, interval=0.25)
            time.sleep(0.07)
            # Press Ctrl+A then Backspace
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.07)
            pyautogui.press('backspace')
            time.sleep(0.07)
            # Enter data from col 2
            pyautogui.write(columns[2])
            time.sleep(0.07)
            # Press tab once
            pyautogui.press('tab')
            time.sleep(0.07)
            # Press enter
            pyautogui.press('enter')
            time.sleep(0.07)
            # Initial click
            pyautogui.click(x_initial, y_initial)
            time.sleep(0.07)
            # Press tab 5 times
            pyautogui.press('tab', presses=5, interval=0.25)
            time.sleep(0.07)
            # Press enter
            pyautogui.press('enter')
            time.sleep(0.07)
            
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