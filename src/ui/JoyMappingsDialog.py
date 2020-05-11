from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import PyQt5

import ExceptionLogger
import ui.JoyMappingsDialogUI
import Options

class JoyMappingsDialog(QtWidgets.QDialog, ui.JoyMappingsDialogUI.Ui_JoyMappingsDialog):
    def __init__(self, joysticks, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        self.model = JoyMappingDataModel(joysticks)
        self.mappingTable.setModel(self.model)
        self.delegate = JoyMappingDelegate(self)
        self.mappingTable.setItemDelegate(self.delegate)
        self.mappingTable.horizontalHeader().setStretchLastSection(True)
        self.restoreGeometry(Options.get("Mappings-dialog-geometry", QtCore.QByteArray()))
        self.mappingTable.restoreGeometry(Options.get("Mappings-dialog-mappings-table-geometry", QtCore.QByteArray()))
        self.okCancelBtn.accepted.connect(lambda: ExceptionLogger.logException(self._accept))
        self.okCancelBtn.rejected.connect(lambda: ExceptionLogger.logException(self._reject))
        self.mappingTable.setColumnWidth(0, int(Options.get("Mappings-dialog-table-width", 100)))
        self.returnData = None

    def getMappings(self):
        return self.returnData

    def _accept(self):
        self._savePositions()
        self.returnData = self.model.getModel()

    def _reject(self):
        self._savePositions()

    def _savePositions(self):
        Options.set("Mappings-dialog-geometry", self.saveGeometry())
        Options.set("Mappings-dialog-mappings-table-geometry", self.mappingTable.saveGeometry())
        Options.set("Mappings-dialog-table-width", self.mappingTable.columnWidth(0))



class JoyMappingDataModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent = None):
        super(QtCore.QAbstractTableModel, self).__init__(parent)
        self.dataItem = data

    def getModel(self):
        return self.dataItem

    def flags(self, index):
        if index.column() == 0:
            return PyQt5.Qt.Qt.ItemIsEnabled
        else:
            return PyQt5.Qt.Qt.ItemIsSelectable | PyQt5.Qt.Qt.ItemIsEditable | PyQt5.Qt.Qt.ItemIsEnabled

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.dataItem)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 2

    def setData(self, index, value, role):
        if not index.isValid() or role != QtCore.Qt.DisplayRole:
            return False

        self.dataItem[index.row()][1] = None if value == 0 else value

        return True

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if index.column() == 0:
            guidTxt = "".join([hex(i)[2:] for i in self.dataItem[index.row()][0][0]])
            nameTxt = self.dataItem[index.row()][0][1]
            return QtCore.QVariant("{0} ({1})".format(nameTxt, guidTxt))
        else:
            if self.dataItem[index.row()][1] is None:
                return QtCore.QVariant("not in use")
            else:
                return QtCore.QVariant(int(self.dataItem[index.row()][1]))


class JoyMappingDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent = None):
        super(QtWidgets.QStyledItemDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            return super(QtWidgets.QStyledItemDelegate, self).createEditor(parent, option, index)

        cmbBox = QtWidgets.QComboBox(parent)
        cmbBox.addItem("not is use", None)
        usedIndies = set(map(lambda x: x[1], index.model().getModel())) - set([None])

        for i in range(1, 21):
            if i not in usedIndies:
                cmbBox.addItem("{0}".format(i), i)
        self._setCmbBox(index, cmbBox)

        return cmbBox

    def setEditorData(self, editor, index):
        if index.column() == 0:
            super(QtWidgets.QStyledItemDelegate, self).setEditorData(editor, index)

        if type(editor) is QtWidgets.QComboBox:
            self._setCmbBox(index, editor)

    def _setCmbBox(self, index, editor):
        value = index.model().data(index, QtCore.Qt.DisplayRole)
        for i in range(editor.count()):
            correctValue = 0 if value.type() == QtCore.QVariant.String else value.value()
            if editor.itemData(i) == correctValue:
                editor.setCurrentIndex(i)
                break

    def setModelData(self, editor, model, index):
        if index.column() == 0:
            super(QtWidgets.QStyledItemDelegate, self).setModelData(editor, model, index)

        joyIndex = editor.currentData()

        index.model().setData(index, joyIndex, QtCore.Qt.DisplayRole)