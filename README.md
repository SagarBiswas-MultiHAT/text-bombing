# Auto Typing Script

This Python script uses the `pyautogui` library to automatically type and send the text "Hello World" repeatedly in any active text field. It waits for 3 seconds before starting, then continuously types and presses "Enter". This can be useful for automating simple tasks or testing purposes.

## Features

- Automatically types "Hello World" and presses "Enter".
- Simple and easy-to-use automation script.
- Uses the `pyautogui` library for keyboard control.

## Requirements

- Python 3.x
- `pyautogui` library

You can install the required library using:

```bash
pip install pyautogui
```

## Setting Up a Virtual Environment

For better package management and to avoid conflicts with your system environment, it's recommended to use a virtual environment.

### Steps:

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Install `pyautogui` inside the virtual environment:
    ```bash
    pip install pyautogui
    ```

4. Deactivate the virtual environment when you're done:
    ```bash
    deactivate
    ```

## How to Use

1. Clone or download the script.
2. Run the script in your terminal:
    ```bash
    python3 auto_typing_script.py
    ```
3. After the 3-second delay, the script will start typing "Hello World" and pressing "Enter" continuously.

### Example Output

The script will type:
```
Hello World
```
and press "Enter" repeatedly.

## License

This project is licensed under the MIT License.
