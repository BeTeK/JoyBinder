

class Joystick:
    def __init__(self, guid):
        self.guid = guid
        self.curData = None
        self.prevData = None

    def ready(self):
        return self.curData is not None and self.prevData is not None

    def setData(self, data):
        self.prevData = self.curData
        self.curData = data

    def getAxises(self, new):
        if new:
            return self.curData.axises
        else:
            return self.prevData.axises

    def getButtons(self, new):
        if new:
            return self.curData.buttons
        else:
            return self.prevData.buttons

    def getGuid(self):
        return self.guid

    def getName(self):
        return self.curData.name

    def isButtonPressed(self, btnNum):
        return self.curData[btnNum]