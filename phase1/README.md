# Phase 1 — `sys`, `os`, and `pathlib`

A deeper pass over the same theme as Phase 0: knowing exactly where your
script runs and what its environment looks like. Phase 1 introduces
`pathlib` and starts wrapping environment info into reusable functions
instead of loose top-level code.

## Files

| File | What it does |
|------|--------------|
| `probe.py` | Prints the interpreter, the CWD, and every file in the CWD using `Path.cwd().iterdir()`. |
| `functions_probe.py` | Defines `describe_environment()`, which returns a dict describing the environment. |
| `data2.txt` | Sample data file. |
| `reflection.md`, `reflection2.md` | Written reflection notes. |

## Key lesson

`functions_probe.py` moves from "print things" to "return things":

```python
def describe_environment():
    return {
        "python_executable": sys.executable,
        "current_working_directory": str(Path.cwd()),
        "script_directory": str(Path(__file__).parent),
        "files_in_current_directory": [f.name for f in Path.cwd().iterdir() if f.is_file()],
    }
```

Returning structured data (a dict) instead of printing makes the logic
reusable and testable — the first step toward writing real backend code.

## Running

```bash
python3 phase1/probe.py
python3 phase1/functions_probe.py
```
