import time

import pynput
from RemoteHotKey.Utility.KeyboardMouseActionPerformer import KeyboardMouseActionPerformer
from RemoteHotKey.ActionManager import ActionManager


class MainActionManager(ActionManager):
    _actionPerformer = None

    def __init__(self, actionPerformer: KeyboardMouseActionPerformer):
        super().__init__()
        self._actionPerformer = actionPerformer

    def _shouldStartOneTimeAction(self) -> bool:
        for event in self._currentState.getEventLog():
            if event.getName() in ['ButtonClicked']:
                self.event = event
                event.handle()
                return True
        return False

    def _oneTimeAction(self):
        if self.event.getName() == 'ButtonClicked':
            print(self.event.getData().get("print"))
        self.event = None
        return

    def _shouldStartRoutineAction(self) -> bool:
        if self._currentState.getFromStorage("PrintTotalToTerminalRepeatedlyToggle"):
            return True
        return False

    def _shouldEndRoutineAction(self) -> bool:
        return not self._shouldStartRoutineAction()

    def _routineAction(self):
        v = self._currentState.getFromStorage("NumberToggleTotalValue")
        print(f"Total Value: {v}")
        time.sleep(1.0)
        return
