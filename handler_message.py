from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()

state = ""
def keyboard(command):
    if command == "j":
        k.tap_key("j")
    elif command == "k":
        k.tap_key("k")
    elif command =="jk":
        k.press_keys(["j","k"])
    elif command == "kl":
        k.tap_key("kl")
    elif command == "jjj":
        k.press_key("w")
keyboard("jjj")
while(True):
    # keyboard("jjj")
    time.sleep(1)
