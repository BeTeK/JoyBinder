
import model.VJoyJoystick

class VJoyJoysticks:
    def __init__(self):
        self.joystics = {}

    def getJoy(self, index):
        if index not in self.joystics:
            self.joystics[index] = model.VJoyJoystick.VJoyJoystick(index)

        return self.joystics[index]

    def update(self):
        for joy in self.joystics.values():
            joy.update()




