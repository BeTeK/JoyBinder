
import model.VJoyJoysticks
import ScriptRunner

def buildScriptRunner():
    vjoy = model.VJoyJoysticks.VJoyJoysticks()
    runner = ScriptRunner.ScriptRunner(vjoy)
    return runner
