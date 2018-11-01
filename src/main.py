import sys
from PyQt5 import QtWidgets
import ui
import ui.MainDialog
import XInputReader.XInputReader

def showUI(options):
    with XInputReader.XInputReader() as reader:
        app = QtWidgets.QApplication(sys.argv)
        ex = ui.MainDialog.MainDialog(reader)
        ex.show()
        sys.exit(app.exec_())

def main():
    index = 1
    options = {"operation" : showUI}

    while index < len(sys.argv):
        index += 1

    options["operation"](options)

if __name__ == "__main__":
  main()