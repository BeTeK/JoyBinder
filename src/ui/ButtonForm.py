from PyQt5 import QtWidgets, QtGui
from ui.ButtonFormUI import Ui_ButtonForm
from ResManager import ResManager


class ButtonForm(QtWidgets.QWidget, Ui_ButtonForm):
    def __init__(self, btnName):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)
        self.status = True
        self.buttonNameLabel.setText(btnName)
        self.setStatus(True)

    def setStatus(self, status):
        if status and not self.status:
            self.imageLabel.setPixmap(ResManager().get().btnDownImg)
        elif not status and self.status:
            self.imageLabel.setPixmap(ResManager().get().btnUpImg)

        self.status = status
