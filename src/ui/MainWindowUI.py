# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1321, 753)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1178, 692))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainHLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainHLayout.setContentsMargins(0, 0, 0, 0)
        self.mainHLayout.setObjectName("mainHLayout")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.quitMenuItem = QtWidgets.QAction(MainWindow)
        self.quitMenuItem.setObjectName("quitMenuItem")
        self.openMenuItem = QtWidgets.QAction(MainWindow)
        self.openMenuItem.setObjectName("openMenuItem")
        self.saveMenuItem = QtWidgets.QAction(MainWindow)
        self.saveMenuItem.setObjectName("saveMenuItem")
        self.saveAsMenuItem = QtWidgets.QAction(MainWindow)
        self.saveAsMenuItem.setObjectName("saveAsMenuItem")
        self.menuFile.addAction(self.openMenuItem)
        self.menuFile.addAction(self.saveMenuItem)
        self.menuFile.addAction(self.saveAsMenuItem)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quitMenuItem)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.quitMenuItem.setText(_translate("MainWindow", "Quit"))
        self.openMenuItem.setText(_translate("MainWindow", "Open"))
        self.saveMenuItem.setText(_translate("MainWindow", "Save"))
        self.saveAsMenuItem.setText(_translate("MainWindow", "Save as"))

