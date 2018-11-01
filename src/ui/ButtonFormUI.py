# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ButtonForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ButtonForm(object):
    def setupUi(self, ButtonForm):
        ButtonForm.setObjectName("ButtonForm")
        ButtonForm.resize(421, 31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ButtonForm.sizePolicy().hasHeightForWidth())
        ButtonForm.setSizePolicy(sizePolicy)
        ButtonForm.setMaximumSize(QtCore.QSize(16777215, 31))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ButtonForm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonNameLabel = QtWidgets.QLabel(ButtonForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNameLabel.sizePolicy().hasHeightForWidth())
        self.buttonNameLabel.setSizePolicy(sizePolicy)
        self.buttonNameLabel.setObjectName("buttonNameLabel")
        self.horizontalLayout_2.addWidget(self.buttonNameLabel)
        self.imageLabel = QtWidgets.QLabel(ButtonForm)
        self.imageLabel.setText("")
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_2.addWidget(self.imageLabel)

        self.retranslateUi(ButtonForm)
        QtCore.QMetaObject.connectSlotsByName(ButtonForm)

    def retranslateUi(self, ButtonForm):
        _translate = QtCore.QCoreApplication.translate
        ButtonForm.setWindowTitle(_translate("ButtonForm", "Form"))
        self.buttonNameLabel.setText(_translate("ButtonForm", "TextLabel"))

