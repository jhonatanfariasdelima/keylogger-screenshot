import sys

import cx_Freeze

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    options={"build_exe": {"packages": ["pynput", "pyautogui"], "include_files": []}},
    executables=[cx_Freeze.Executable("main.py", base=base)]
)
