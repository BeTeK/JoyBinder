# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\AxisWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AxisWidget(object):
    def setupUi(self, AxisWidget):
        AxisWidget.setObjectName("AxisWidget")
        AxisWidget.resize(400, 92)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AxisWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.axisNameStr = QtWidgets.QLabel(AxisWidget)
        self.axisNameStr.setObjectName("axisNameStr")
        self.horizontalLayout.addWidget(self.axisNameStr)
        self.axisPositionStr = QtWidgets.QLabel(AxisWidget)
        self.axisPositionStr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisPositionStr.setObjectName("axisPositionStr")
        self.horizontalLayout.addWidget(self.axisPositionStr)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.axisPositionSlider = QtWidgets.QSlider(AxisWidget)
        self.axisPositionSlider.setEnabled(False)
        self.axisPositionSlider.setProperty("value", 30)
        self.axisPositionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.axisPositionSlider.setObjectName("axisPositionSlider")
        self.verticalLayout_2.addWidget(self.axisPositionSlider)

        self.retranslateUi(AxisWidget)
        QtCore.QMetaObject.connectSlotsByName(AxisWidget)

    def retranslateUi(self, AxisWidget):
        _translate = QtCore.QCoreApplication.translate
        AxisWidget.setWindowTitle(_translate("AxisWidget", "Form"))
        self.axisNameStr.setText(_translate("AxisWidget", "TextLabel"))
        self.axisPositionStr.setText(_translate("AxisWidget", "TextLabel"))

