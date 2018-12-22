

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

    def getGuid(self):
        return self.guid

    def getName(self):
        return self.curData.name

    def isButtonPressed(self, btnNum):
        