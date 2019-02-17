# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\JoyMappingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import ExceptionLogger


class Ui_JoyMappingsDialog(object):
    def setupUi(self, JoyMappingsDialog):
        JoyMappingsDialog.setObjectName("JoyMappingsDialog")
        JoyMappingsDialog.resize(781, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JoyMappingsDialog.sizePolicy().hasHeightForWidth())
        JoyMappingsDialog.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(JoyMappingsDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mappingTable = QtWidgets.QTableView(JoyMappingsDialog)
        self.mappingTable.setObjectName("mappingTable")
        self.verticalLayout.addWidget(self.mappingTable)
        self.okCancelBtn = QtWidgets.QDialogButtonBox(JoyMappingsDialog)
        self.okCancelBtn.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelBtn.setObjectName("okCancelBtn")
        self.verticalLayout.addWidget(self.okCancelBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(JoyMappingsDialog)
        self.okCancelBtn.accepted.connect(lambda: ExceptionLogger.logException(JoyMappingsDialog.accept()))
        self.okCancelBtn.rejected.connect(lambda: ExceptionLogger.logException(JoyMappingsDialog.reject()))
        QtCore.QMetaObject.connectSlotsByName(JoyMappingsDialog)

    def retranslateUi(self, JoyMappingsDialog):
        _translate = QtCore.QCoreApplication.translate
        JoyMappingsDialog.setWindowTitle(_translate("JoyMappingsDialog", "Joystick mappings"))

