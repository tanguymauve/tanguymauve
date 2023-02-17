import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter"], "include_files": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Tic Tac",
    version="1.0",
    description="Display time",
    options={"build_exe": build_exe_options},
    executables=[Executable("clock.py", base=base)]
)
