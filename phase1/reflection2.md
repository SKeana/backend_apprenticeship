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