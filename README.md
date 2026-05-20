# Backend Apprenticeship

A personal, phase-by-phase journey learning Python from a backend engineer's
perspective. Each phase builds on the previous one — starting with the basics
of how Python finds files and ending with a working FastAPI service.

The project is organised as a sequence of `phase*/` folders. Each phase
contains the code written for that step plus short reflection notes in
markdown.

## Repository layout

```
backend_apprenticeship/
├── phase0/   Python basics: interpreter, paths, file reading
├── phase1/   sys / os / pathlib — knowing where your script is running
├── phase2/   Parsing records from a text file into structured data
├── phase3/   A CLI app built on top of phase 2's patterns
├── phase4/   FastAPI service exposing the same data over HTTP
└── README.md
```

## Phase 0 — Python from a backend point of view

The starting point. Goal: get comfortable running Python and understand the
difference between the interpreter, the current working directory, and where
the script itself lives.

Key files:
- `phase0/hello.py` — first script, prints the interpreter version and the
  file's own path.
- `phase0/location_probe.py` — prints `sys.executable`, `os.getcwd()`, and
  `__file__` side by side so the three are never confused again.
- `phase0/paths/reader.py` — opens `data.txt` using a path built relative to
  the script (`os.path.dirname(__file__)`), not the CWD. This is the lesson:
  scripts should not assume they're being run from their own directory.
- `phase0/Daily Reflection*.md` — written notes from each day.

Run any script with:
```bash
python3 phase0/hello.py
```

## Phase 1 — `sys`, `os`, and `pathlib`

Same theme as phase 0, but deeper. Phase 1 introduces `pathlib` and starts
wrapping environment information into reusable functions.

Key files:
- `phase1/probe.py` — lists every file in the current working directory
  using `Path.cwd().iterdir()`.
- `phase1/functions_probe.py` — `describe_environment()` returns a dict
  describing the executable, CWD, script directory, and files. First step
  toward writing reusable helpers instead of top-level scripts.
- `phase1/reflection.md`, `phase1/reflection2.md` — notes.

## Phase 2 — Parsing structured data

First taste of working with data. `records.txt` is a CSV-like file
(`name,age,role` per line); `processor.py` loads it into a list of dicts
and runs grouping / filtering / aggregation against it.

Functions in `phase2/processor.py`:
- `load_records()` — read the file, return a list of dicts.
- `group_by_role(records)` — group records by their `role`.
- `count_by_role(records)` — count records per role.
- `filter_by_age(records, min_age)` — filter rows by age.
- `group_filter_by_role(records, min_age)` — combine filtering and grouping.
- `oldest_per_role(records)` — pick the oldest record in each role.

Run:
```bash
cd phase2
python3 processor.py
```

## Phase 3 — A CLI app

Phase 3 is where the patterns from phase 2 are turned into something a user
can interact with. The domain switches from generic "records" to World of
Warcraft DPS logs (`player_name,class,role,dps`).

`phase3/app.py` exposes a menu loop that lets the user:
1. Show all logs
2. Show runs by class
3. Show highest DPS by class
4. Show average DPS by class
5. Exit

Run:
```bash
cd phase3
python3 app.py
```

## Phase 4 — FastAPI service ("MyLogs")

The same WoW-logs domain, now served over HTTP with FastAPI and validated
with Pydantic models.

Files:
- `phase4/main.py` — minimal "Hello World" FastAPI app, used to verify the
  setup.
- `phase4/api.py` — the real service. Loads `logs.txt` once at startup and
  exposes endpoints for browsing runs by class, highest DPS, and averages.
- `phase4/.venv/` — local virtualenv (FastAPI, Uvicorn, etc.).

### Endpoints

| Method | Path                              | Description                                |
|--------|-----------------------------------|--------------------------------------------|
| GET    | `/`                               | Health check                               |
| GET    | `/logs`                           | All runs                                   |
| GET    | `/class/{class_name}`             | Runs for a class (optional `?min_dps=`)    |
| GET    | `/class/{class_name}/highest`     | Highest-DPS run for a class                |
| GET    | `/class/{class_name}/average`     | Average DPS for a class                    |
| GET    | `/highest-dps`                    | Highest-DPS run per class                  |
| GET    | `/average-dps`                    | Average DPS per class                      |

### Running the API

```bash
cd phase4
source .venv/bin/activate
uvicorn api:app --reload
```

Then open <http://127.0.0.1:8000/docs> for the interactive Swagger UI.

## Requirements

- Python 3.12+
- For phase 4: FastAPI, Uvicorn, Pydantic (installed inside `phase4/.venv`).

If recreating the environment from scratch:
```bash
cd phase4
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

## Notes

- `REME.MD` is the original short overview kept as a learning artefact.
  This `README.md` is the expanded version.
- Each phase folder also contains the reflection markdown files written
  during the apprenticeship — they capture the "why" behind each step.
