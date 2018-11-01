from PyQt5 import QtWidgets
import ui.AxisWidgetUI


class AxisWidget(QtWidgets.QWidget, ui.AxisWidgetUI.Ui_AxisWidget):
    def __init__(self, min, max, name):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)
        self._min = min
        self._max = max

        self.axisNameStr.setText(name)

        self._currentAxis = 0
        self.axisPositionSlider.setValue(0)
        self.axisPositionSlider.setMinimum(self._min)
        self.axisPositionSlider.setMaximum(self._max)
        self.axisPositionStr.setText(str(self._currentAxis))

    def setAxis(self, val):
        if val != self._currentAxis:
            self._currentAxis = val
            self.axisPositionSlider.setValue(self._currentAxis)
            self.axisPositionStr.setText(str(self._currentAxis))
