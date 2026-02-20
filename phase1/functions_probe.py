import os
import sys
from pathlib import Path

def describe_environment():
    return {
        "python_executable\n": sys.executable,
        "working_directory\n": os.getcwd(),
        "files_in_working_directory\n": [f.name for f in Path.cwd().iterdir() if f.is_file()],
        "file_in_current work directory (list)\n": [f.name for f in Path.cwd().iterdir() if f.is_file()]
    }

print(describe_environment())