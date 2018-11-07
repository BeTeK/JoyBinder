from PyQt5 import QtWidgets, QtCore
import ui.ProfileOptionsUI
import ui.JoyMappingsDialog

class ProfileOptions(ui.ProfileOptionsUI.Ui_ProfileOptions, QtWidgets.QFrame):
    def __init__(self, parent = None):
        super(QtWidgets.QFrame, self).__init__(parent)
        self.setupUi(self)
        self.mappingsBtn.pressed.connect(self._pressed)
        self.joyData = None

    def setJoyData(self, joyData):
        self.joyData = joyData

    def _pressed(self):
        if self.joyData is not None:
            data = []
            for key, value in self.joyData.items():
                data.append([(key, value.getName()), value.getIndex()])

            dialog = ui.JoyMappingsDialog.JoyMappingsDialog(data, self)
            dialog.setModal(True)
            dialog.exec()

            if dialog.getMappings() is not None:
                for i in dialog.getMappings():
                    self.joyData[i[0][0]].setIndex(i[1])

