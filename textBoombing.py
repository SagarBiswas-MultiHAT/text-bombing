import pyautogui as pag
import time

time.sleep(3)

while True:
    pag.typewrite("Hello World")
    pag.press("enter")
    # time.sleep(1)

'''
Use a Virtual Environment
This is the recommended approach for managing Python packages without affecting the system environment.

1. Create a virtual environment:
    python3 -m venv venv

2. Activate the virtual environment:
    source venv/bin/activate

3. Install pyautogui inside the virtual environment:
    pip install pyautogui

4. Deactivate the virtual environment: 
    deactivate
'''