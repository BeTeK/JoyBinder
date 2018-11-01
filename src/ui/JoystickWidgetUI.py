# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\JoystickWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JoystickWidget(object):
    def setupUi(self, JoystickWidget):
        JoystickWidget.setObjectName("JoystickWidget")
        JoystickWidget.resize(437, 817)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JoystickWidget.sizePolicy().hasHeightForWidth())
        JoystickWidget.setSizePolicy(sizePolicy)
        JoystickWidget.setFrameShape(QtWidgets.QFrame.Panel)
        JoystickWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        JoystickWidget.setLineWidth(5)
        JoystickWidget.setMidLineWidth(2)
        self.joyDataLayout = QtWidgets.QVBoxLayout(JoystickWidget)
        self.joyDataLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.joyDataLayout.setObjectName("joyDataLayout")
        self.joyNameStr = QtWidgets.QLabel(JoystickWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joyNameStr.sizePolicy().hasHeightForWidth())
        self.joyNameStr.setSizePolicy(sizePolicy)
        self.joyNameStr.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.joyNameStr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.joyNameStr.setLineWidth(3)
        self.joyNameStr.setMidLineWidth(1)
        self.joyNameStr.setObjectName("joyNameStr")
        self.joyDataLayout.addWidget(self.joyNameStr)

        self.retranslateUi(JoystickWidget)
        QtCore.QMetaObject.connectSlotsByName(JoystickWidget)

    def retranslateUi(self, JoystickWidget):
        _translate = QtCore.QCoreApplication.translate
        JoystickWidget.setWindowTitle(_translate("JoystickWidget", "Frame"))
        self.joyNameStr.setText(_translate("JoystickWidget", "TextLabel"))

