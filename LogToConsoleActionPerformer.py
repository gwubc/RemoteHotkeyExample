import inspect
from RemoteHotKey.Utility.KeyboardMouseActionPerformer import KeyboardMouseActionPerformer


class LogToConsoleActionPerformer(KeyboardMouseActionPerformer):

    def __init__(self):
        super().__init__()

    def leftClick(self):
        print(inspect.currentframe().f_code.co_name)

    def rightClick(self):
        print(inspect.currentframe().f_code.co_name)

    def tapKeyboard(self, key):
        print(inspect.currentframe().f_code.co_name, key)

    def keyDown(self, key, dur=None):
        super().keyDown(key, dur)

        if self.downKeys[key] == 1:
            print(f"keyDown {key}")

    def keyUp(self, key):
        super().keyUp(key)
        print(f"keyUp {key}")

    def print(self, str):
        print(inspect.currentframe().f_code.co_name, str)

