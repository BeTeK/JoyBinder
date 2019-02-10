import traceback
import sys

def logException(fn):
    try:
        fn()
    except Exception as ex:
        print(ex)
        traceback.print_exc(file=sys.stdout)
        raise ex
