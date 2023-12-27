import time
import typing
from uuid import uuid4

from RemoteHotKey.WebUI.Button import Button
from RemoteHotKey.OneTimeEvent import OneTimeEvent
from RemoteHotKey.State import State
from RemoteHotKey.WebUI.UITemplate import UIPage, UITemplate
from RemoteHotKey.Utility.KeyboardMouseActionPerformer import KeyboardActions, MouseActions


class EventButton(Button):
    _eventName = None
    _eventData = None

    def __init__(self, label, eventName, eventData: typing.Dict, rowspan=1, colspan=1):
        super().__init__(str(uuid4()), label, rowspan=rowspan, colspan=colspan)
        self._eventName = eventName
        self._eventData = eventData

    def getUI(self, currentState: State) -> typing.Dict:
        self._backgroundColor = Button.defaultColor
        return self._jsonDic()

    def updateState(self, currentState: State, event: typing.Dict) -> None:
        currentState.store(State.Keys.mostRecentUIElementId, self._identifier)
        event = OneTimeEvent()
        event.setFields(self._eventName, time.time(), self._eventData)
        currentState.addOneTimeEvent(event)
        return None


class PageChangeButton(Button):
    pageOffSet: int
    def __init__(self, label, pageOffSet, rowspan=1, colspan=1):
        super().__init__(str(uuid4()), label, rowspan=rowspan, colspan=colspan)
        self.pageOffSet = pageOffSet

    def updateState(self, currentState: State, event: typing.Dict) -> None:
        if self.pageOffSet > 0:
            UITemplate.nextPage(currentState)
        elif self.pageOffSet < 0:
            UITemplate.nextPage(currentState)
        return None


class NumberToggle(Button):
    _eventData: typing.Dict

    def __init__(self, label, eventData: typing.Dict, rowspan=1, colspan=1):
        super().__init__(str(uuid4()), label, rowspan=rowspan, colspan=colspan)
        self._eventData = eventData

    def getUI(self, currentState: State) -> typing.Dict:
        self._backgroundColor = Button.defaultColor
        if currentState.getFromStorage(self._identifier):
            self._backgroundColor = Button.highlightColor
        return self._jsonDic()

    def updateState(self, currentState: State, event: typing.Dict) -> None:
        v = currentState.getFromStorage("NumberToggleTotalValue", 0)
        if currentState.getFromStorage(self._identifier):
            currentState.store(self._identifier, None)
            currentState.store("NumberToggleTotalValue", v - self._eventData.get("value", 0))
        else:
            currentState.store(self._identifier, True)
            currentState.store("NumberToggleTotalValue", v + self._eventData.get("value", 0))
        return None

class NumberToggleTotalValueDisplay(Button):

    def __init__(self, rowspan=1, colspan=1):
        super().__init__(str(uuid4()), "", rowspan=rowspan, colspan=colspan)

    def getUI(self, currentState: State) -> typing.Dict:
        self._backgroundColor = Button.defaultColor
        d = self._jsonDic()
        v = currentState.getFromStorage("NumberToggleTotalValue", 0)
        d["label"] = f"Total: {v}"
        return d

    def updateState(self, currentState: State, event: typing.Dict) -> None:
        return None

class PrintTotalToTerminalRepeatedlyToggle(Button):

    def __init__(self):
        super().__init__("PrintTotalToTerminalRepeatedlyToggle", "Print Total To Terminal Repeatedly", rowspan=1, colspan=3)

    def getUI(self, currentState: State) -> typing.Dict:
        self._backgroundColor = Button.defaultColor
        if currentState.getFromStorage(self._identifier):
            self._backgroundColor = Button.highlightColor
        return self._jsonDic()

    def updateState(self, currentState: State, event: typing.Dict) -> None:
        if currentState.getFromStorage("PrintTotalToTerminalRepeatedlyToggle"):
            currentState.store("PrintTotalToTerminalRepeatedlyToggle", None)
        else:
            currentState.store("PrintTotalToTerminalRepeatedlyToggle", True)
        return None


def createTemplate() -> UITemplate:
    template = UITemplate("main")

    page1 = UIPage((3, 3))

    page1.addUIElement(PageChangeButton("Next Page", 1))
    page1.addUIElement(EventButton("B1", "ButtonClicked", {"print": "B1 clicked"}, 2))
    page1.addUIElement(EventButton("B2", "ButtonClicked", {"print": "B2 clicked"}, 3))
    page1.addUIElement(EventButton("B3", "ButtonClicked", {"print": "B3 clicked"}, 1, 2))
    page1.addUIElement(EventButton("B4", "ButtonClicked", {"print": "B4 clicked"}))

    page2 = UIPage((3, 3))
    page2.addUIElement(PageChangeButton("Next Page", 1))
    page2.addUIElement(NumberToggle("1", {"value": 1}))
    page2.addUIElement(NumberToggle("3", {"value": 3}))
    page2.addUIElement(NumberToggle("7",  {"value": 7}))
    page2.addUIElement(NumberToggle("-5",  {"value": -5}))
    page2.addUIElement(NumberToggleTotalValueDisplay())
    page2.addUIElement(PrintTotalToTerminalRepeatedlyToggle())

    page3 = UIPage((3, 3))
    page3.addUIElement(PageChangeButton("Go to page 1", -2))
    page3.addUIElement(EventButton("a", "Keyboard", {"action": KeyboardActions.TapKeyboard, "Key": "a"}))
    page3.addUIElement(EventButton("b", "Keyboard", {"action": KeyboardActions.TapKeyboard, "Key": "b"}))
    page3.addUIElement(EventButton("Mouse LeftClick", "Mouse", {"action": MouseActions.LeftClick}))

    template.addPage(page1)
    template.addPage(page2)
    template.addPage(page3)
    return template


