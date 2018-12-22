import model.Joystick
from functools import reduce

class Joysticks:
    def __self__(self, reader):
        self.joysticks = {}
        self.reader = reader

    def poll(self):
        joysticksChanged = False
        curData = self.reader.poll()
        if set(self.joysticks.keys()) != set([i.guid for i in curData]):
            self.joysticks.clear()
            for i in curData:
                self.joysticks[i.guid] = model.Joystick.Joystick(i.guid)

            joysticksChanged = True

        for i in curData:
            self.joysticks[i.guid].setData(i)

        return joysticksChanged

    def ready(self):
        readyLst = map(lambda x: x.ready(), self.joysticks.values())
        return reduce(lambda left, right: left and right, readyLst)

    def rescan(self):
        self.reader.rescan()

    def getJoysticks(self):
        return self.joysticks




