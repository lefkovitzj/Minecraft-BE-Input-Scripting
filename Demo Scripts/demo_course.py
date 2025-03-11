"""
Custom Script Name:
Custom Script Description:
Custom Script Author:
Custom Script Last Modified:

Project Name: Minecraft BE Input Scripting
Project Author: Joseph Lefkovitz (github.com/lefkovitzj)
"""

from MC_Manipulation import *
import pyautogui
import time

def bridge(instance):
    instance.look_down(degree=180)
    instance.start_crouch()
    instance.look_up(degree=2)
    instance.start_backward()
    time.sleep(0.1)
    for j in range(32):
        time.sleep(1 / BASE_CROUCH_SPEED + 0.1)
        instance.place()
    instance.stop_backward()
    instance.stop_crouch()
    instance.look_up(degree=88)
    instance.look_left(degree=180)

def equip_armor(instance):
    for i in range(4):
        instance.select_slot(4+i)
        instance.use_item()
        time.sleep(0.1)

def empty_bundle(instance):
    instance.select_slot(3)
    time.sleep(0.1)
    for i in range(6):
        instance.use_item()
        time.sleep(0.25)

def two_jumps(instance):
    instance.look_up(degree=90)
    time.sleep(0.25)
    instance.start_sprint()
    instance.start_forward()
    time.sleep(0.15)
    instance.jump()
    time.sleep(0.6)
    instance.jump()
    time.sleep(0.47)
    instance.stop_forward()
    instance.stop_sprint()

def get_crossbow(instance):
    instance.look_right(90)
    time.sleep(0.25)
    instance.start_forward()
    time.sleep(5.6/BASE_WALK_SPEED)
    instance.stop_forward()
    time.sleep(0.25)
    instance.look_up(120)
    time.sleep(0.1)
    instance.select_slot(4)
    time.sleep(0.1)
    instance.use_item()
    time.sleep(0.1)
    instance.select_slot(1)

def hit_targets(instance):
    time.sleep(0.25)
    instance.look_down(degree=90)
    instance.load_crossbow(quick_charge=1, fire_after=True)
    time.sleep(0.25)
    instance.look_left(90)
    instance.load_crossbow(quick_charge=1)
    instance.use_item()
    time.sleep(0.25)
    instance.look_left(90)
    instance.load_crossbow(quick_charge=1)
    time.sleep(0.25)
    instance.look_left(90)
    time.sleep(0.25)
    instance.use_item()
    instance.look_right(90)
    time.sleep(0.25)

def plant_tree(instance):
    instance.start_forward()
    time.sleep(10.5/BASE_WALK_SPEED)
    instance.stop_forward()
    time.sleep(0.25)
    instance.look_down(45)
    time.sleep(0.25)
    instance.select_slot(6)
    time.sleep(0.1)
    instance.use_item()
    time.sleep(0.25)
    instance.select_slot(5)
    time.sleep(0.1)
    for i in range(12):
        instance.use_item()
        time.sleep(0.1)
    time.sleep(0.15)
    instance.look_up(45)
    time.sleep(0.25)
    instance.attack_destroy(hold_time=3.1)
    time.sleep(0.25)

def collect_water(instance):
    instance.look_right(90)
    time.sleep(0.1)
    instance.look_right(90)
    time.sleep(0.25)
    instance.start_forward()
    time.sleep(4.25/BASE_WALK_SPEED)
    instance.stop_forward()
    time.sleep(0.25)
    instance.look_left(90)
    time.sleep(0.25)
    instance.start_forward()
    time.sleep(5.5/BASE_WALK_SPEED)
    instance.stop_forward()
    time.sleep(0.25)
    instance.look_down(90)
    time.sleep(0.25)
    instance.select_slot(7)
    instance.use_item()
    time.sleep(0.25)
    instance.start_forward()
    time.sleep(0.5/BASE_WALK_SPEED)
    instance.stop_forward()
    time.sleep(0.25)

def bridge_across(instance):
    instance.look_left(90)
    time.sleep(0.25)
    instance.look_left(90)
    instance.select_slot(8)
    time.sleep(0.25)
    instance.start_crouch()
    instance.look_up(1)
    instance.start_backward()
    time.sleep(0.1)
    for i in range(8):
        time.sleep(1 / BASE_CROUCH_SPEED + 0.1)
        instance.place()
    instance.stop_backward()
    instance.stop_crouch()
    instance.look_right(90)
    time.sleep(0.25)
    instance.look_right(90)
    time.sleep(0.25)

def fall_down(instance):
    instance.select_slot(7)
    instance.start_forward()
    time.sleep(1.0/BASE_WALK_SPEED)
    instance.stop_forward()
    instance.look_down(15)
    instance.use_item(hold_time=0.15)
    time.sleep(0.25)


def custom_script(instance):
    equip_armor(instance)
    empty_bundle(instance)
    two_jumps(instance)
    get_crossbow(instance)
    hit_targets(instance)
    plant_tree(instance)
    collect_water(instance)
    bridge_across(instance)
    fall_down(instance)



if __name__ == "__main__":
    pyautogui.countdown(7)
    MC = Instance()
    custom_script(MC) # Use this code to run the custom script defined above.
    del MC # Ensure that "del MC" ends the file to clean up after any unresolved keypresses.