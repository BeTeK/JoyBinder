
import pyvjoy

class VJoyJoystick:
    def __init__(self, devNro):
        self.dev = pyvjoy.VJoyDevice(devNro)
        self.buttonBanks = {0: (self._setBank1, self._getBank1),
                            1: (self._setBank2, self._getBank2),
                            2: (self._setBank3, self._getBank3),
                            3: (self._setBank4, self._getBank4)}

        self.axises = {1: self.setAxis01,
                       2: self.setAxis02,
                       3: self.setAxis03,
                       4: self.setAxis04,
                       5: self.setAxis05,
                       6: self.setAxis06,
                       7: self.setAxis07,
                       8: self.setAxis08,
                       9: self.setAxis09,
                       10: self.setAxis10,
                       11: self.setAxis11,
                       12: self.setAxis12,
                       13: self.setAxis13,
                       14: self.setAxis14,
                       15: self.setAxis15,
                       16: self.setAxis16,
                       17: self.setAxis17}

        self.updated = False

    def setAxis(self, axisNro, value):
        self.updated = True
        if axisNro not in self.axises:
            raise Exception("Cannot find axis {0}".format(axisNro))

        self.axises[axisNro](value)

    def setButton(self, btnNro, down):
        self.updated = True
        bankIndex = btnNro // 32
        buttonNro = btnNro % 32
        bank = self.buttonBanks[bankIndex]
        currentStates = bank[1]()
        if down:
            currentStates = currentStates | (1 << buttonNro)
        else:
            currentStates = currentStates & (0xffffffff ^ (1 << buttonNro))
        bank[0](currentStates)

    def update(self):
        if self.updated:
            self.dev.update()
            self.updated = False

    def _setBank1(self, states):
        self.dev.data.lButtons = states

    def _setBank2(self, states):
        self.dev.data.lButtonsEx1 = states

    def _setBank3(self, states):
        self.dev.data.lButtonsEx2 = states

    def _setBank4(self, states):
        self.dev.data.lButtonsEx3 = states

    def _getBank1(self):
        return self.dev.data.lButtons

    def _getBank2(self):
        return self.dev.data.lButtonsEx1

    def _getBank3(self):
        return self.dev.data.lButtonsEx2

    def _getBank4(self):
        return self.dev.data.lButtonsEx3

    def setAxis01(self, value):
        self.dev.data.wThrottle = value

    def setAxis02(self, value):
        self.dev.data.wRudder = value

    def setAxis03(self, value):
        self.dev.data.wAileron = value

    def setAxis04(self, value):
        self.dev.data.wAxisX = value

    def setAxis05(self, value):
        self.dev.data.wAxisY = value

    def setAxis06(self, value):
        self.dev.data.wAxisZ = value

    def setAxis07(self, value):
        self.dev.data.wAxisXRot = value

    def setAxis08(self, value):
        self.dev.data.wAxisYRot = value

    def setAxis09(self, value):
        self.dev.data.wAxisZRot = value

    def setAxis10(self, value):
        self.dev.data.wSlider = value

    def setAxis11(self, value):
        self.dev.data.wDial = value

    def setAxis12(self, value):
        self.dev.data.wWheel = value

    def setAxis13(self, value):
        self.dev.data.wAxisVX = value

    def setAxis14(self, value):
        self.dev.data.wAxisVY = value

    def setAxis15(self, value):
        self.dev.data.wAxisVZ = value

    def setAxis16(self, value):
        self.dev.data.wAxisVBRX = value

    def setAxis17(self, value):
        self.dev.data.wAxisVRBY = value

