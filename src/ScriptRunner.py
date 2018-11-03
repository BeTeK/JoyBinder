
import pyautogui

class ScriptRunner:
    def __init__(self):
        self.txt = ""
        self.globals = {}
        self.actions = {}
        self.curTime = None
        self.prevState = None
        self.curState = None
        self._makeGlobals()

    def _makeGlobals(self):
        self.globals.clear()
        self.globals["onAlways"] = self._onAlways
        self.globals["onJoyBtnDown"] = self._onJoyBtnDown
        self.globals["onJoyBtnUp"] = self._onJoyBtnUp
        self.globals["delay"] = self._delayCommand
        self.globals["setBtnDown"] = self._setButtonDownCommand
        self.globals["setBtnUp"] = self._setButtonUpCommand
        self.globals["setKeyDown"] = self._setKeyDownCommad
        self.globals["setKeyUp"] = self._setKeyUpCommad

    def setScript(self, txt):
        self.txt = txt

    def runScript(self, prevState, curState, curTime):
        self.curTime = curTime
        self.prevState = prevState
        self.curState = curState
        self.globals["curState"] = curState
        self.globals["prevState"] = prevState

        try:
            exec(self.txt, self.globals)
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)

        self._executeQueue(curTime)

    def _executeQueue(self, time):
        queuesToExecute = sorted(filter(lambda x: x <= time, self.actions.keys()))
        for i in queuesToExecute:
            queue = self.actions[i]
            for cmd in queue:
                cmd()

            del self.actions[i]

    def _onJoyBtnDown(self, joyId, btnIndex, *params):
        if not self.prevState[int(joyId)].buttons[btnIndex] and self.curState[int(joyId)].buttons[btnIndex]:
            self._addToQueue(params)

    def _onJoyBtnUp(self, joyId, btnIndex, *params):
        if self.prevState[int(joyId)].buttons[btnIndex] and not self.curState[int(joyId)].buttons[btnIndex]:
            self._addToQueue(params)

    def _onAlways(self, *params):
        self._addToQueue(params)

    def _addToQueue(self, commands):
        curTime = self.curTime
        for i in commands:
            if type(i) is float:
                curTime = i
            else:
                if curTime not in self.actions:
                    self.actions[curTime] = []

                queue = self.actions[curTime]
                queue.append(i)


    def _delayCommand(self, time):
        return self.curTime + (time / 1000.0)

    def _setButtonDownCommand(self, joyId):
        return lambda: self._setButton(joyId, True)

    def _setButtonUpCommand(self, joyId):
        return lambda: self._setButton(joyId, False)

    def _setButton(self, joyId, down):
        print("push joy {0} state {1}".format(joyId, down))

    def _setKeyDownCommad(self, key):
        return lambda: self._setKey(key, True)

    def _setKeyUpCommad(self, key):
        return lambda: self._setKey(key, False)

    def _setKey(self, key, down):
        if down:
            pyautogui.keyDown(key)
        else:
            pyautogui.keyUp(key)

        print("push key {0} state {1}".format(key, down))
