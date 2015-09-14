import sys
PyVersion = sys.version_info[0] 

if PyVersion == 2:
    from .py2.classfitfunc import *
    from .py2.helpers import *
    
elif PyVersion == 3:
    print("importing from py3 ...")
    from .py3 import classfitfunc
    from .py3.classfitfunc import *
    from .py3 import helpers
    print("done.")
