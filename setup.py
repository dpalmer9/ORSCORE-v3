import sys
import os
from cx_Freeze import setup, Executable

current_dir = os.getcwd()
exp_folder = "\\Experiments"
protocol_folder = "\\Protocols"
exp_dir = current_dir + exp_folder
protocol_dir = current_dir + protocol_folder
sys.path.insert(0,exp_dir)
sys.path.insert(0,protocol_dir)

os.environ['TCL_LIBRARY'] = r"C:\Users\dpalmer\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\dpalmer\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6"


build_exe_options = {"packages": ["os", "tkinter", "time", "threading", "imp", "SORv14"], "excludes": [""], "include_files": [r"C:\Users\dpalmer\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\dpalmer\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"] }

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name="ORScorev3",version="1.0",description="OR Score Program", options={"build_exe": build_exe_options}, executables = [Executable('ORSCorev31Main.py', base=base)])
