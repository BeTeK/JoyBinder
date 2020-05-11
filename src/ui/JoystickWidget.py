from PyQt5 import QtWidgets
import ui.JoystickWidgetUI
import ui.ButtonForm
import ui.AxisWidget

class JoystickWidget(QtWidgets.QFrame, ui.JoystickWidgetUI.Ui_JoystickWidget):
    def __init__(self, joy):
        super(QtWidgets.QFrame, self).__init__()
        self.joy = joy
        self.setupUi(self)
        self.buttonWidgets = []

        self.axisWidgets = []

        for i in range(len(self.joy.getAxises(True))):
            axis = ui.AxisWidget.AxisWidget(0, (1 << 16) - 1, "Axis {0}".format(i + 1))
            axis.setAxis(self.joy.getAxises(True)[i])

            self.axisWidgets.append(axis)
            self.joyDataLayout.addWidget(axis)

        for i in range(len(self.joy.getButtons(True))):
            btn = ui.ButtonForm.ButtonForm("button {0}".format(i + 1))
            btn.setStatus(self.joy.getButtons(True)[i])

            self.buttonWidgets.append(btn)
            self.joyDataLayout.addWidget(btn)

        self.joyNameStr.setText(joy.getName())
        self.index = None

    def update(self):

        for index, value in enumerate(self.joy.getButtons(True)):
            self.buttonWidgets[index].setStatus(value)

        for index, value in enumerate(self.joy.getAxises(True)):
            self.axisWidgets[index].setAxis(value)


    def getGUID(self):
        return self.joy.getGuid()

    def getName(self):
        return self.joy.getName()

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index
