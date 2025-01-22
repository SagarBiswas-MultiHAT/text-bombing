import pyautogui
import time

message = input("\n..:: Enter the message to be bombed\t\t\t: ")

while True:
    try:
        count = int(input("..:: Enter the number of times to send the message\t: "))
        if count <= 0:
            raise ValueError("The count must be a positive integer.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        delay_input = input("..:: Enter the delay (in seconds) between each message\t: ")
        if delay_input == '':
            delay = 0
        else:
            delay = float(delay_input)
        if delay < 0:
            raise ValueError("The delay must be a non-negative number.")
        break
    except ValueError as e:
        print(e)

print("\n\t\t==> Starting message bombing...")
for i in range(3, 0, -1): # Countdown from 3 to 1
    print(i)
    time.sleep(1)
print("\n\t!. BOMBING!")

for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(delay)

print("\n\n ..:: Message bombing completed ::..\n\n")
