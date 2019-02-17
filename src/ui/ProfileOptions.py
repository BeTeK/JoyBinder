from PyQt5 import QtWidgets, QtCore

import ExceptionLogger
import ui.ProfileOptionsUI
import ui.JoyMappingsDialog

class ProfileOptions(ui.ProfileOptionsUI.Ui_ProfileOptions, QtWidgets.QFrame):
    def __init__(self, parent = None):
        super(QtWidgets.QFrame, self).__init__(parent)
        self.setupUi(self)
        self.mappingsBtn.pressed.connect(lambda: ExceptionLogger.logException(self._pressed()))
        self.joyData = None
        self.joyIndies = {}

    def setJoyData(self, joyData):
        if self.joyData is not joyData:
            self.joyData = joyData
            self._genJoyIndex()

    def getJoyIndies(self):
        return self.joyIndies

    def setJoyIndies(self, indies):
        self.joyIndies = indies

    def _genJoyIndex(self):
        self.joyIndies = {}
        for key, value in self.joyData.items():
            if value.getIndex() is not None:
                self.joyIndies[value.getIndex()] = value.getGUID()

    def _getGuidToIndex(self):
        ret = {}
        for key, value in self.joyIndies.items():
            ret[value] = key

        return ret

    def _pressed(self):
        if self.joyData is not None:
            data = []
            guidToIndex = self._getGuidToIndex()
            for key, value in self.joyData.items():
                index = value.getIndex()

                if value.getGUID() in guidToIndex:
                    index = guidToIndex[value.getGUID()]

                data.append([(key, value.getName()), index])

            dialog = ui.JoyMappingsDialog.JoyMappingsDialog(data, self)
            dialog.setModal(True)
            dialog.exec()

            if dialog.getMappings() is not None:
                for i in dialog.getMappings():
                    self.joyData[i[0][0]].setIndex(i[1])

                self._genJoyIndex()

