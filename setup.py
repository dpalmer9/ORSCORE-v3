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

os.environ['TCL_LIBRARY'] = r"C:\Python34\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python34\tcl\tk8.6"


build_exe_options = {"packages": ["os", "tkinter", "time", "threading", "imp", "SORv14", "MSOv10", "pandas", "numpy"], "excludes": [""], "include_files": [r"C:\Python34\DLLs\tcl86t.dll",
                 r"C:\Python34\DLLs\tk86t.dll"] }

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name="ORScorev3",version="1.0",description="OR Score Program", options={"build_exe": build_exe_options}, executables = [Executable(r'C:\Users\dpalmer\PycharmProjects\ORScore3_32_Compatible\ORScorev31Main.py', base=base)])
