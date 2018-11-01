from PyQt5 import QtWidgets

class TextEditor(QtWidgets.QTextEdit):
    def __init__(self):
        super(QtWidgets.QTextEdit, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
