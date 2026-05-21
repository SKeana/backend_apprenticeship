# Phase 4 — FastAPI service ("MyLogs")

The same WoW-logs domain as Phase 3, now served over HTTP with FastAPI and
validated with Pydantic models. This is the step from "a program on my
machine" to "a backend other programs can call".

> The original short overview lives in `REME.md`; this file is the expanded
> version.

## Files

| File | What it does |
|------|--------------|
| `main.py` | Minimal "Hello World" FastAPI app — used to verify the setup. |
| `api.py` | The real service: loads `logs.txt` and exposes the API. |
| `logs.txt` | Data file — one run per line: `player_name,class,role,dps`. |
| `notes.md` | Notes — the run command. |
| `REME.md` | Original short overview. |
| `.venv/` | Local virtualenv (FastAPI, Uvicorn, Pydantic, etc.). |

## Endpoints (`api.py`)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check. |
| GET | `/logs` | All runs. |
| GET | `/class/{class_name}` | Runs for a class — optional `?min_dps=` filter. |
| GET | `/class/{class_name}/highest` | Highest-DPS run for a class. |
| GET | `/class/{class_name}/average` | Average DPS for a class. |
| GET | `/highest-dps` | Highest-DPS run per class. |
| GET | `/average-dps` | Average DPS per class. |

Unknown classes / empty filter results return `404` via `HTTPException`.

## Pydantic models

- `Run` — a single run (`player_name`, `class_name`, `role`, `dps`).
- `RunListResponse` — `count` + a list of `Run`.
- `AverageResponse` — `class_name` + `average_dps`.

These are used as `response_model`s so FastAPI validates and documents the
output automatically.

## Key lesson

The data-loading and analysis functions are nearly identical to Phase 3 —
what's new is the HTTP layer: routing, path/query parameters, typed
response models, and proper error responses.

## Running

```bash
cd phase4
source .venv/bin/activate
uvicorn api:app --reload
```

Then open the interactive Swagger docs:

- API: <http://127.0.0.1:8000/>
- Docs: <http://127.0.0.1:8000/docs>

To run the minimal hello-world app instead: `uvicorn main:app --reload`.

## Recreating the environment

```bash
cd phase4
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```
