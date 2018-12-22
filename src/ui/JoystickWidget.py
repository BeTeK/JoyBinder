from PyQt5 import QtWidgets
import ui.JoystickWidgetUI
import ui.ButtonForm
import ui.AxisWidget

class JoystickWidget(QtWidgets.QFrame, ui.JoystickWidgetUI.Ui_JoystickWidget):
    def __init__(self, name):
        super(QtWidgets.QFrame, self).__init__()
        self.setupUi(self)
        self.buttonWidgets = []

        self.axisWidgets = []

        for i in range(len(self.data.axises)):
            axis = ui.AxisWidget.AxisWidget(0, (1 << 16) - 1, "Axis {0}".format(i + 1))
            axis.setAxis(self.data.axises[i])

            self.axisWidgets.append(axis)
            self.joyDataLayout.addWidget(axis)

        for i in range(len(self.data.buttons)):
            btn = ui.ButtonForm.ButtonForm("button {0}".format(i + 1))
            btn.setStatus(self.data.buttons[i])

            self.buttonWidgets.append(btn)
            self.joyDataLayout.addWidget(btn)

        self.joyNameStr.setText(name)
        self.index = None

    def setJoyData(self, data):
        self.data = data
        for index, value in enumerate(self.data.buttons):
            self.buttonWidgets[index].setStatus(value)

        for index, value in enumerate(self.data.axises):
            self.axisWidgets[index].setAxis(value)


    def getGUID(self):
        return self.data.guid

    def getName(self):
        return self.data.name

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index
