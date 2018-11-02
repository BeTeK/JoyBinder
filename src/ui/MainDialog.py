from PyQt5 import QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
import ui.JoystickWidget
import ui.TextEditor
import Options
import ScriptRunner
import time

class MainDialog(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, reader):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setupUi(self)
        self.quitMenuItem.triggered.connect(self._quit)

        self.inputReader = reader
        self.inputReader.rescan()

        self.lastData = None
        self.curData = None
        self.scriptRunner = ScriptRunner.ScriptRunner()

        self.joysticks = {}
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._onPollTimerTimeout)
        self.timer.start(1000/100)
        self._rebuildSticks()

        self.expertEditor = ui.TextEditor.TextEditor()
        self.mainHLayout.addWidget(self.expertEditor)

        self.restoreGeometry(Options.get("MainWindow-geometry", QtCore.QByteArray()))
        self.restoreState(Options.get("MainWindow-state", QtCore.QByteArray()))
        self.splitter.restoreGeometry(Options.get("MainWindow-splitter-geometry", QtCore.QByteArray()))
        self.splitter.restoreState(Options.get("MainWindow-splitter-state", QtCore.QByteArray()))



    def _onPollTimerTimeout(self):
        self.lastData = self.curData
        self.curData = self.inputReader.poll()

        if set(self.joysticks.keys()) != set([i.guid for i in self.curData]):
            self._rebuildSticks()

        for i in self.curData:
            self.joysticks[i.guid].setJoyData(i)

        self.scriptRunner.setScript(self.expertEditor.getCode())
        if self.lastData is not None and self.curData is not None:
            self.scriptRunner.runScript(self.lastData, self.curData, time.time())


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

    def closeEvent(self, event):
        Options.set("MainWindow-geometry", self.saveGeometry())
        Options.set("MainWindow-state", self.saveState())
        Options.set("MainWindow-splitter-geometry", self.splitter.saveGeometry())
        Options.set("MainWindow-splitter-state", self.splitter.saveState())

    def _quit(self):

        self.close()

