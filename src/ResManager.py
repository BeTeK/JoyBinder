from PyQt5 import QtGui
import os.path


class ResManager:
    class __ResManager:
        def __init__(self):
            self.rootPath = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(os.path.realpath(__file__))), ".."))
            self.btnDownImg = QtGui.QPixmap(os.path.join(self.rootPath, "icons", "buttonDown.png"))
            self.btnUpImg = QtGui.QPixmap(os.path.join(self.rootPath, "icons", "buttonUp.png"))

    instance = None

    def __init__(self):
        if ResManager.instance is None:
            ResManager.instance = ResManager.__ResManager()

    def get(self):
        return ResManager.instance
