import os
import sys
from pathlib import Path

print("Python executable:")
print(sys.executable)

print("\n current working directory:")
print(os.getcwd())

print("\n All files in directory:")
phase1_path = Path.cwd() / "phase1"

for item in phase1_path.iterdir():
    if item.is_file():
        print(item.name)