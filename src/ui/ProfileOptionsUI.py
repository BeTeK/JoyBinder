# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ProfileOptions.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProfileOptions(object):
    def setupUi(self, ProfileOptions):
        ProfileOptions.setObjectName("ProfileOptions")
        ProfileOptions.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ProfileOptions)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mappingsBtn = QtWidgets.QPushButton(ProfileOptions)
        self.mappingsBtn.setObjectName("mappingsBtn")
        self.horizontalLayout.addWidget(self.mappingsBtn)

        self.retranslateUi(ProfileOptions)
        QtCore.QMetaObject.connectSlotsByName(ProfileOptions)

    def retranslateUi(self, ProfileOptions):
        _translate = QtCore.QCoreApplication.translate
        ProfileOptions.setWindowTitle(_translate("ProfileOptions", "Frame"))
        self.mappingsBtn.setText(_translate("ProfileOptions", "Mappings"))

