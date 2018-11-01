from PyQt5 import QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
import ui.JoystickWidget
import ui.TextEditor


class MainDialog(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, reader):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setupUi(self)
        self.quitMenuItem.triggered.connect(self._quit)

        self.inputReader = reader
        self.inputReader.rescan()

        self.lastData = None
        self.curData = None

        self.joysticks = {}
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._onPollTimerTimeout)
        self.timer.start(1000/100)
        self._rebuildSticks()

        self.mainHLayout.addWidget(ui.TextEditor.TextEditor())

    def _onPollTimerTimeout(self):
        self.lastData = self.curData
        self.curData = self.inputReader.poll()

        if set(self.joysticks.keys()) != set([i.guid for i in self.curData]):
            self._rebuildSticks()

        for i in self.curData:
            self.joysticks[i.guid].setJoyData(i)


    def _rebuildSticks(self):

        while self.verticalLayout.count() > 0:
            item = self.verticalLayout.takeAt(0)
            self.verticalLayout.removeItem(item)

        self.joysticks.clear()
        if self.curData is not None:
            for i in self.curData:
                self.joysticks[i.guid] = ui.JoystickWidget.JoystickWidget(i)

        for i in self.joysticks.values():
            self.verticalLayout.addWidget(i)

        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def _quit(self):
        self.close()

