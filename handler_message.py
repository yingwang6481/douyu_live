#coding=utf-8
from comb import *
import re
m = PyMouse()
k = PyKeyboard()

def keyboard(command):

    if command == "j":
        k.press_key("j")
        time.sleep(0.1)
        k.release_key("j")
    elif command == "k":
        k.tap_key("k")
    elif command =="jk":
        k.press_keys(["j","k"])
    elif command == "kl":
        k.tap_key("kl")
    elif command == "jjj":
        k.press_key("a")


def msg_handler(msg):
    print msg
    actions = re.split(",|，", msg)
    for action in actions:
        commands = action.split("+")
        if len(commands)>0:
            if len(commands)==2 and commands[0] in ["star1","star2","star3","star4","star5","star6","combo1","combo2"]:
                combo.combo_handler(commands)
            else:
                action_control.action_handler(commands)
def restart():
    k.tap_key(k.alt_l_key)
    k.tap_key("f")
    k.tap_key(k.down_key,5)
    k.tap_key(k.enter_key)

