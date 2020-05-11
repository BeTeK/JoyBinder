
import pyautogui
pyautogui.FAILSAFE = False

class ScriptRunner:
    def __init__(self, vjoy):
        self.vjoy = vjoy
        self.txt = ""
        self.globals = {}
        self.actions = {}
        self.curTime = None
        self.joysticks = None
        self.joyIndies = None
        self.codeAdded = False
        self._makeGlobals()

    def _makeGlobals(self):
        self.codeAdded = False

        self.globals = {}
        self.globals["onAlways"] = self._onAlways
        self.globals["onJoyBtnDown"] = self._onJoyBtnDown
        self.globals["onJoyBtnUp"] = self._onJoyBtnUp
        self.globals["onJoyAxisEnters"] = self._onJoyAxisEnters
        self.globals["onJoyAxisExits"] = self._onJoyAxisExits
        self.globals["onJoyAxisRange"] = self._onJoyAxisRange
        self.globals["delay"] = self._delayCommand
        self.globals["setBtnDown"] = self._setButtonDownCommand
        self.globals["setBtnUp"] = self._setButtonUpCommand
        self.globals["setKeyDown"] = self._setKeyDownCommad
        self.globals["setKeyUp"] = self._setKeyUpCommad
        self.globals["setJoyKeyUp"] = self._setJoyKeyUpCommad
        self.globals["setJoyKeyDown"] = self._setJoyKeyDownCommad
        self.globals["setMouseKeyDown"] = self._setMouseKeyDownCommand
        self.globals["setMouseUpDown"] = self._setMouseKeyUpCommand
        self.globals["setJoyAxis"] = self._setJoyAxisCommand
        self.globals["getJoyAxis"] = self._getJoyAxisCommand
        self.globals["getJoyBtn"] = self._getJoyBtnCommand
        self.globals["btn"] = self._btnId
        self.globals["axis"] = self._axisId

    def setScript(self, txt):
        self.txt = txt
        self._makeGlobals()

    def runScript(self, joyModel, joyIndies, curTime):
        self.curTime = curTime
        self.joysticks = joyModel
        self.joyIndies = joyIndies
        self.globals["joyModel"] = joyModel

        try:
            exec(self.txt, self.globals)

            self._executeQueue(curTime)
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

        self.vjoy.update()

    def _getJoyBtn(self, id, new):
        if id[2] != "btn":
            raise Exception("Wrong type of id. type is {0} should be btn".format(id[2]))

        joyId = self.joyIndies[id[0]]
        return self.joysticks.getJoystick(joyId).getButtons(new)[id[1]]

    def _getJoyAxis(self, id, new):
        if id[2] != "axis":
            raise Exception("Wrong type of id. type is {0} should be axis".format(id[2]))

        joyId = self.joyIndies[id[0]]
        return self.joysticks.getJoystick(joyId).getAxises(new)[id[1]]

    def _btnId(self, joyIndex, btnIndex):
        return (joyIndex, btnIndex - 1, "btn")

    def _axisId(selfs, joyIndex, axisIndex):
        return (joyIndex, axisIndex - 1, "axis")

    def _executeQueue(self, time):
        queuesToExecute = sorted(filter(lambda x: x <= time, self.actions.keys()))
        for i in queuesToExecute:
            queue = self.actions[i]
            for cmd in queue:
                cmd()

            del self.actions[i]

    def _onJoyBtnDown(self, id, *params):
        if not self._getJoyBtn(id, False) and self._getJoyBtn(id, True):
            self._addToQueue(params)

    def _onJoyBtnUp(self, id, *params):
        if self._getJoyBtn(id, False) and not self._getJoyBtn(id, True):
            self._addToQueue(params)

    def _onJoyAxisRange(self, id, left, right, *params):
        minAxisVal = min(left, right)
        maxAxisVal = max(left, right)
        curVal = self._getJoyAxis(id, True)

        if minAxisVal <= curVal and curVal <= maxAxisVal:
            self._addToQueue(params)


    def _onJoyAxisExits(self, id, left, right, *params):
        minAxisVal = min(left, right)
        maxAxisVal = max(left, right)

        prevVal = self._getJoyAxis(id, False)
        curVal = self._getJoyAxis(id, True)

        if not (minAxisVal <= curVal and curVal <= maxAxisVal) and minAxisVal <= prevVal and prevVal <= maxAxisVal:
            self._addToQueue(params)

    def _onJoyAxisEnters(self, id, left, right, *params):
        minAxisVal = min(left, right)
        maxAxisVal = max(left, right)
        prevVal = self._getJoyAxis(id, False)
        curVal = self._getJoyAxis(id, True)

        if minAxisVal <= curVal and curVal <= maxAxisVal and not (minAxisVal <= prevVal and prevVal <= maxAxisVal):
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
        # print("push joy {0} state {1}".format(joyId, down))
        pass

    def _setKeyDownCommad(self, key):
        return lambda: self._setKey(key, True)

    def _setKeyUpCommad(self, key):
        return lambda: self._setKey(key, False)

    def _setKey(self, key, down):
        if down:
            pyautogui.keyDown(key)
        else:
            pyautogui.keyUp(key)

        #print("push key {0} state {1}".format(key, down))

    def _setJoyKeyUpCommad(self, joyIndex, keyIndex):
        return lambda: self.vjoy.getJoy(joyIndex).setButton(keyIndex, False)

    def _setJoyKeyDownCommad(self, joyIndex, keyIndex):
        return lambda: self.vjoy.getJoy(joyIndex).setButton(keyIndex, True)

    def _setJoyAxisCommand(self, joyIndex, axisIndex, value):
        return lambda: self.vjoy.getJoy(joyIndex).setAxis(axisIndex, int(value * (2**15 + 1)))

    def _getJoyAxisCommand(self, id, current = True):
        val = self._getJoyAxis(id, current)
        return val / 2**16

    def _getJoyBtnCommand(self, id, current = True):
        val = self._getJoyBtn(id, current)
        return val

    def _setMouseKeyDownCommand(self, key):
        pyautogui.mouseDown(button=key)

    def _setMouseKeyUpCommand(self, key):
        pyautogui.mouseUp(button=key)