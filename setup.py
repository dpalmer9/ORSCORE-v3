import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "tkinter", "time", "threading", "imp"], "excludes": [""]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="ORScorev3",version="1.0",description="OR Score Program", options={"build_exe": build_exe_options}, executables = [Executable('ORSCorev31Main.py', base=base)])
