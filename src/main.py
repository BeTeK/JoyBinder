import sys
from PyQt5 import QtWidgets
import ui
import ui.MainDialog
import XInputReader.XInputReader
import model.Joysticks
import ExceptionLogger
import ProfileFile
import time
import ScriptRunnerFactory

def showUI(options):
    sys.stdout = sys.stderr

    with XInputReader.XInputReader() as reader:
        app = QtWidgets.QApplication(sys.argv)
        joysticks = model.Joysticks.Joysticks(reader)
        ex = ui.MainDialog.MainDialog(joysticks)
        ex.show()
        sys.exit(app.exec_())

def runProgram(options):
    with XInputReader.XInputReader() as reader:
        joysticks = model.Joysticks.Joysticks(reader)
        joysticks.rescan()
        file = ProfileFile.ProfileFile()
        file.load(options["fileToOpen"])
        runner = ScriptRunnerFactory.buildScriptRunner()
        runner.setScript(file.getCode())
        mappings = file.getJoyMappings()
        while True:
            joysticks.poll()
            if joysticks.ready():
                runner.runScript(joysticks, mappings, time.time())



def main():
    index = 1
    options = {"operation" : showUI,
               "fileToOpen" : None}

    while index < len(sys.argv):
        if "-f" in sys.argv[index] or "--file" in sys.argv[index]:
            index += 1
            options["fileToOpen"] = sys.argv[index]
        elif "--gui" in sys.argv[index]:
            options["operation"] = showUI
        elif "--no-gui" in sys.argv[index]:
            options["operation"] = runProgram
        index += 1

    ExceptionLogger.logException(lambda :options["operation"](options))


if __name__ == "__main__":
    main()

