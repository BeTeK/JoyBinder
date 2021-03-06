from PyQt5 import QtWidgets
from ExceptionLogger import logException

class TextEditor(QtWidgets.QTextEdit):
    def __init__(self):
        super(QtWidgets.QTextEdit, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.textChanged.connect(lambda : logException(self._onCodeChanged))
        self.changedText = None

    def _onCodeChanged(self):
        self.changedText = self.toPlainText()

    def getCodeIfChanged(self):
        ret = None
        if self.changedText is not None:
            ret = self.changedText
            self.changedText = None

        return ret

    def getCode(self):
        return self.toPlainText()

    def setCode(self, txt):
        self.changedText = txt
        self.setText(txt)

