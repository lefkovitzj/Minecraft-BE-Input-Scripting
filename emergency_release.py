import pyautogui
def release_all(down_keys):
    """Releases all pressed keys and mouse buttons."""
    try:
        for key in down_keys:
            pyautogui.keyUp(key)

    except Exception as e:
        print(f"Error releasing keys/buttons: {e}")

if __name__ == "__main__":
    release_all(pyautogui.KEYBOARD_KEYS)