# Phase 0 — Python from a backend point of view

The starting point of the apprenticeship. The goal is to get comfortable
running Python and to understand three things that are easy to confuse:

- the **interpreter** running your code (`sys.executable`)
- the **current working directory** (`os.getcwd()`)
- where the **script file itself** lives (`__file__`)

## Files

| File | What it does |
|------|--------------|
| `hello.py` | First script — prints `sys.version` and the file's own path. |
| `location_probe.py` | Prints the interpreter path, the CWD, and `__file__` side by side. |
| `paths/reader.py` | Opens `paths/data.txt` using a path built relative to the script. |
| `paths/data.txt` | Sample data read by `reader.py`. |
| `response.md`, `Daily Reflection*.md` | Written reflection notes. |

## Key lesson

`paths/reader.py` builds its file path from the script location, not the
current working directory:

```python
Base_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(Base_DIR, "data.txt")
```

This means the script works no matter what folder you run it from — a
script should never assume it's launched from its own directory.

## Running

```bash
python3 phase0/hello.py
python3 phase0/location_probe.py
python3 phase0/paths/reader.py
```
