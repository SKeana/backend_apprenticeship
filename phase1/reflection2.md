Code:
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

output:
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ python3 functions_probe.py
{'python_executable\n': '/usr/bin/python3', 'working_directory\n': '/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1', 'files_in_working_directory\n': ['probe.py', 'reflection.md', 'data2.txt', 'functions_probe.py', 'reflection2.md'], 'file_in_current work directory (list)\n': ['probe.py', 'reflection.md', 'data2.txt', 'functions_probe.py', 'reflection2.md']}

---
I've really got no idea how to change the presentation but I look over and got ride of an import that I wasn't using.
import sys
from pathlib import Path

def describe_environment():
    return {
        "python_executable": sys.executable,
        "current_working_directory": str(Path.cwd()),
        "script_directory": str(Path(__file__).parent),
        "files_in_current_directory": [f.name for f in Path.cwd().iterdir() if f.is_file()],
    }
print(describe_environment())