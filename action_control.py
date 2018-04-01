#coding=utf-8
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()
long_action_state ={
    "w":0,
    "s":0,
    "a":0,
    "d":0,
    "j":0,
    "k":0,
    "u":0,
    "i":0
}
long_action2short_action = {
    "www":"w",
    "sss":"s",
    "aaa":"a",
    "ddd":"d",
    "jjj":"j",
    "kkk":"k",
    "uuu":"u",
    "iii":"i"
}
class action_control:
    @staticmethod
    def clear():
        k.release_key("w")
        k.release_key("s")
        k.release_key("a")
        k.release_key("d")
        k.release_key("j")
        k.release_key("k")
        k.release_key("u")
        k.release_key("i")
    @staticmethod
    def short_action(commands):
        for command in commands:
            k.press_key(command)
            time.sleep(0.05)
            k.release_key(command)
    @staticmethod
    def short_actions(commands):
        for command in commands:
            k.press_key(command)
        time.sleep(0.05)
        for command in commands:
            k.release_key(command)

    @staticmethod
    def long_actions(commands):
        for command in commands:
            command = long_action2short_action[command]
            if long_action_state[command]==0:
                k.press_key(command)
                long_action_state[command] = 1
            else:
                k.release_key(command)
    @staticmethod
    def combo(commands):
        for command in commands:
            if isinstance(command,list):
                action_control.short_actions(command)
            else:
                k.press_key(command)
                time.sleep(0.05)
                k.release_key(command)
    @staticmethod
    def action_handler(commands):
        short_commands = []
        long_commands = []
        for command in commands:
            if command in ['w','s','a','d','j','k','u','i']:
                short_commands.append(command)
            elif command in ["www",'sss','aaa','ddd','jjj','kkk','uuu','iii']:
                long_commands.append(command)
        action_control.short_actions(short_commands)
        action_control.long_actions(long_commands)
        if len(commands)>0:
            if commands[0]=="投币":
                action_control.short_actions([k.function_keys[3]])
            if commands[0]=="开始":
                action_control.short_actions([k.function_keys[1]])
