import time

from RemoteHotKey.Utility.KeyboardMouseActionPerformer import KeyboardMouseActionPerformer, KeyboardActions, MouseActions
from RemoteHotKey.ActionManager import ActionManager
from RemoteHotKey.OneTimeEvent import OneTimeEvent


class KeyboardAndMouseActionManager(ActionManager):
    _actionPerformer: KeyboardMouseActionPerformer

    def __init__(self, actionPerformer: KeyboardMouseActionPerformer):
        super().__init__()
        self._actionPerformer = actionPerformer

    def _shouldStartOneTimeAction(self) -> bool:
        for event in self._currentState.getEventLog():
            if event.getName() in ['Keyboard', 'Mouse']:
                self.event = event
                event.handle()
                return True
        return False

    def _handleKeyboard(self, event: OneTimeEvent):
        key = event.getData().get("Key")
        action = event.getData().get("action")
        if not (key and action):
            return
        if action == KeyboardActions.keyUp:
            self._actionPerformer.keyUp(key)
        elif action == KeyboardActions.keyDown:
            self._actionPerformer.keyDown(key)
        elif action == KeyboardActions.TapKeyboard:
            self._actionPerformer.tapKeyboard(key)

    def _handleMouse(self, event: OneTimeEvent):
        action = event.getData().get("action")
        if not action:
            return
        if action == MouseActions.LeftClick:
            self._actionPerformer.leftClick()
        elif action == MouseActions.RightClick:
            self._actionPerformer.rightClick()
        elif action == MouseActions.MoveMouseTo:
            x = event.getData().get("x")
            y = event.getData().get("y")
            if x and y:
                self._actionPerformer.moveMouseTo(x, y)


    def _oneTimeAction(self):
        if self.event.getName() == 'Keyboard':
            self._handleKeyboard(self.event)
        elif self.event.getName() == 'Mouse':
            self._handleMouse(self.event)

        self.event = None
        return

    def _shouldStartRoutineAction(self) -> bool:
        if self._currentState.getFromStorage("repeat"):
            return True
        return False

    def _shouldEndRoutineAction(self) -> bool:
        return not self._shouldStartRoutineAction()

    def _routineAction(self):
        for keyboardActions in self._currentState.getFromStorage("keyboardActions"):
            self._handleKeyboard(keyboardActions)
        for mouseActions in self._currentState.getFromStorage("mouseActions"):
            self._handleKeyboard(mouseActions)
        time.sleep(self._currentState.getFromStorage("repeatInterval", 1))
        return
