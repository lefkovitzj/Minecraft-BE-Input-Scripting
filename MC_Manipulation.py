import pyautogui
import time
import csv

def hold_key (hold_time, key_code):
    pyautogui.keyDown(key_code)
    time.sleep(hold_time)
    pyautogui.keyUp(key_code)

def release_all(down_keys):
    """Releases all pressed keys and mouse buttons."""
    try:
        for key in down_keys:
            pyautogui.keyUp(key)

    except Exception as e:
        print(f"Error releasing keys/buttons: {e}")


TIME_TO_DEG = 0.01

class Instance():
    def __init__(self, hotbar_slot = 1):
        """ Initialize the object instance. """
        # Store two angles (as in spherical coordinate system with degrees) for player view direction.
        self.phi = 90
        self.theta = 0
        self.current_hotbar_slot = hotbar_slot
        #self.movement_type = ["normal"] # Can be from "normal", "sneaking", "sprinting", "jumping".
        self.down_keys = []

    def look_right(self, degree=90):
        """ Move the camera angle right. """
        hold_key(TIME_TO_DEG * degree, "right")
        self.theta += degree
    def look_left(self, degree=90):
        """ Move the camera angle left. """
        hold_key(TIME_TO_DEG * degree, "left")
        self.theta -= degree
    def look_up(self, degree=90):
        """ Move the camera angle up. """
        hold_key(TIME_TO_DEG * degree, "up")
        self.phi -= degree
    def look_down(self, degree=90):
        """ Move the camera angle down. """
        hold_key(TIME_TO_DEG * degree, "down")
        self.phi += degree


    # Handle player movement.
    def start_sprint(self):
        self.down_keys.append("ctrl")
        pyautogui.keyDown("ctrl")
    def stop_sprint(self):
        pyautogui.keyUp("ctrl")
        self.down_keys.remove("ctrl")
    def start_crouch(self):
        self.down_keys.append("shift")
        pyautogui.keyDown("shift")
    def stop_crouch(self):
        pyautogui.keyUp("shift")
        self.down_keys.remove("shift")
    def jump(self):
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")



    def start_forward(self):
        self.down_keys.append("w")
        pyautogui.keyDown("w")
    def stop_forward(self):
        pyautogui.keyUp("w")
        self.down_keys.remove("w")
    def start_backward(self):
        self.down_keys.append("s")
        pyautogui.keyDown("s")
    def stop_backward(self):
        pyautogui.keyUp("s")
        self.down_keys.remove("s")
    def start_left_strafe(self):
        self.down_keys.append("a")
        pyautogui.keyDown("a")
    def stop_left_strafe(self):
        pyautogui.keyUp("a")
        self.down_keys.remove("a")
    def start_right_strafe(self):
        self.down_keys.append("d")
        pyautogui.keyDown("d")
    def stop_right_strafe(self):
        pyautogui.keyUp("d")
        self.down_keys.remove("d")


    # Handle HUD movement.
    def select_slot(self, slot_num, scroll=False):
        """ Select a hotbar slot, either direct or by scroll. """
        if slot_num == self.current_hotbar_slot: # No slot change needed.
            return
        elif not scroll: # Go directly to the hotbar slot.
            pyautogui.press(f"{slot_num}")
            self.current_hotbar_slot = slot_num
        else: # Scroll to the hotbar slot.
            difference = slot_num - self.current_hotbar_slot
            sign = difference/abs(difference)
            if abs(difference) > 4:
                sign *= -1
                difference = 9-difference
            for i in range(abs(difference)):
                pyautogui.scroll(int(sign) * -1)

    # Handle base player action functionality.
    def use_item(self, slot=None, hold_time=None):
        """ Use the item in hand. """
        if slot!= None:
            self.select_slot(slot)
        if hold_time == None:
            pyautogui.click(button="right")
        else:
            pyautogui.mouseDown(button="right")
            time.sleep(hold_time)
            pyautogui.mouseUp(button="right")

    def attack_destroy(self, slot=None, hold_time=None):
        """ Use the item in hand. """
        if slot!= None:
            self.select_slot(slot)
        if hold_time == None:
            pyautogui.click(button="left")
        else:
            pyautogui.mouseDown(button="left")
            time.sleep(hold_time)
            pyautogui.mouseUp(button="left")

    # Handle pre-defined player actions.
    def place(self, slot=None):
        """ Place the block in hand. """
        if slot!= None:
            self.select_slot(slot)
        self.use_item(slot=slot, hold_time=None)

    def eat(self, slot=None, number=1, is_kelp=False):
        """ Eat/drink one consumable. """
        for i in range(number):
            self.use_item(slot=slot, hold_time=1.61 if not is_kelp else 0.865) # Time per https://minecraft.wiki/w/Food.
    def shoot_bow(self, slot=None):
        """ Charge a bow fully and fire. """
        if slot!= None:
            self.select_slot(slot)
        self.use_item(hold_time=1.0) # Time per https://minecraft.wiki/w/Bow.
    def load_crossbow(self, slot=None, quick_charge=0, fire_after = False):
        """ Charge a crossbow (accounting for quick charge, and optionally fire after charge. """
        if slot!= None:
            self.select_slot(slot)
        self.use_item(hold_time = 1.25 - (0.25 * quick_charge)) # Time per http://minecraft.wiki/w/Quick_Charge.
        if fire_after:
            time.sleep(0.25)
            self.use_item()
    def use_trident(self, slot=None):
        """ Charge and use a trident (riptide or otherwise). """
        if slot!= None:
            self.select_slot(slot)
        instance.use_item(hold_time = 0.382) # Time based on trial and error, not listed on wiki.
    def __del__(self):
        release_all(self.down_keys)


if __name__ == "__main__":
    pyautogui.countdown(5)
    instance = MC_Manipulation(hotbar_slot=1)
    instance.start_sprint()
    instance.start_forward()
    for i in range(10):
        time.sleep(0.5)
        instance.jump()

    del instance
