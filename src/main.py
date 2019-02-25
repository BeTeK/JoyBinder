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
import threading
from mem_top import mem_top
from pympler.tracker import SummaryTracker


def showUI(options):
    sys.stdout = sys.stderr

    with XInputReader.XInputReader() as reader:
        app = QtWidgets.QApplication(sys.argv)
        joysticks = model.Joysticks.Joysticks(reader)
        ex = ui.MainDialog.MainDialog(joysticks)
        ex.show()
        sys.exit(app.exec_())

def runnerTimer(options):
    with XInputReader.XInputReader() as reader:
        joysticks = model.Joysticks.Joysticks(reader)
#        joysticks.rescan()
#        joysticks.poll()
        file = ProfileFile.ProfileFile()
        file.load(options["fileToOpen"])
        runner = ScriptRunnerFactory.buildScriptRunner()
        runner.setScript(file.getCode())
        mappings = file.getJoyMappings()
        counter = 0
        tracker = SummaryTracker()
        while True:
            counter += 1
            if joysticks.ready():
                pass
                #runner.runScript(joysticks, mappings, time.time())

#            joysticks.poll()
            tracker.print_diff()
            if counter > 10000:
                print(mem_top())
                counter = 0

            #time.sleep(1 / 100)


def runProgram(options):
    t = threading.Thread(target=runnerTimer, args=(options, ))
    t.run()
    t.join()

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
