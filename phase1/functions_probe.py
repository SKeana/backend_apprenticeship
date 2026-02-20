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