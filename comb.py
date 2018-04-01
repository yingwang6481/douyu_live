from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
from action_control import action_control
m = PyMouse()
k = PyKeyboard()

class combo:
    @staticmethod
    def star1(commands):
        action_control.combo(["s",["s","a"],"d",commands])

    @staticmethod
    def star2(commands):
        action_control.combo(["s",["s","d"],"a",commands])

    @staticmethod
    def star3(commands):
        action_control.combo(["s","d","s","d",commands])

    @staticmethod
    def star4(commands):
        action_control.combo(["s","a","s","a",commands])
    @staticmethod
    def star5(commands):
        action_control.combo(["d","s","a","d","s","a",commands])

    @staticmethod
    def star6(commands):
        action_control.combo(["a","s","d","a","s","d",commands])

    @staticmethod
    def combo1(commands):
        action_control.combo(["s",["s","d"],"d",commands])
        time.sleep(0.05)
        action_control.combo(["s",["s","d"],"d",commands])
        time.sleep(0.05)
        action_control.combo(["s",["s","d"],"d",commands])
        time.sleep(0.05)

    @staticmethod
    def combo2(commands):
        action_control.combo(["s",["s","a"],"a",commands])
        time.sleep(0.05)
        action_control.combo(["s",["s","a"],"a",commands])
        time.sleep(0.05)
        action_control.combo(["s",["s","a"],"a",commands])
        time.sleep(0.05)
    @staticmethod
    def combo_handler(commands):
        if commands[0] == "star1":
            if commands[1] in ["j","u","k","i"]:
                combo.star1(commands[1:])
        elif commands[0] == "star2":
            if commands[1] in ["j","u","k","i"]:
                combo.star2(commands[1:])
        elif commands[0] == "star3":
            if commands[1] in ["j","u","k","i"]:
                combo.star3(commands[1:])
        elif commands[0] == "star4":
            if commands[1] in ["j","u","k","i"]:
                combo.star4(commands[1:])
        elif commands[0] == "star5":
            if commands[1] in ["j","u","k","i"]:
                combo.star5(commands[1:])
        elif commands[0] == "star6":
            if commands[1] in ["j","u","k","i"]:
                combo.star6(commands[1:])
        elif commands[0] == "combo1":
            if commands[1] in ["j","u","k","i"]:
                combo.combo1(commands[1:])
        elif commands[0] == "combo2":
            if commands[1] in ["j","u","k","i"]:
                combo.combo2(commands[1:])
