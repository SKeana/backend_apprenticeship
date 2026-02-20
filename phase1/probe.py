import os
import sys
from pathlib import Path

print("Python executable:")
print(sys.executable)

print("\n current working directory:")
print(os.getcwd())

print("\nAll files in current working directory:")

for item in Path.cwd().iterdir():
    if item.is_file():
        print(item.name)