import traceback
import sys
import os.path
from os.path import expanduser

def logException(fn):
    try:
        fn()
    except Exception as ex:
        home = expanduser("~")
        path = os.path.join(home, "joyBinder.error.log")
        with open(path, "a") as f:
            traceback.print_exc(file=f)
            f.write("\n")
        traceback.print_exc(file=sys.stdout)
        raise ex
