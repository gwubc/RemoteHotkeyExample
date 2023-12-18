import pynput
from ahk import AHK
from RemoteHotKey.Utility.KeyboardMouseActionPerformer import KeyboardMouseActionPerformer
from RemoteHotKey.Utility.ActionPerformer_Pynput import ActionPerformer_Pynput


# Use ahk for mouse, use pynput for keyboard
class AHKActionPerformer(KeyboardMouseActionPerformer):
    _ahk = None
    _ActionPerformer_Pynput = None

    def __init__(self):
        super().__init__()
        self._ahk = AHK()
        self._ActionPerformer_Pynput = ActionPerformer_Pynput(pynput.keyboard.Controller(), pynput.mouse.Controller())

    def leftClick(self):
        self._ahk.click()

    def rightClick(self):
        self._ahk.right_click()

    def tapKeyboard(self, key):
        self._ActionPerformer_Pynput.tapKeyboard(key)

    def keyDown(self, key, dur=None):
        super().keyDown(key, dur)

        if self.downKeys[key] == 1:
            if type(key) == type(""):
                self._ahk.key_down(key)
            elif key == pynput.keyboard.Key.ctrl:
                self._ahk.key_down('Control')
            else:
                self._ActionPerformer_Pynput.keyDown(key)

    def keyUp(self, key):
        super().keyUp(key)
        if type(key) == type(""):
            self._ahk.key_up(key)
        elif key == pynput.keyboard.Key.ctrl:
            self._ahk.key_up('Control')
        else:
            self._ActionPerformer_Pynput.keyUp(key)

    def print(self, str):
        print(str)

    