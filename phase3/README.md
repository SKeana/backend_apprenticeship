# Phase 3 — A CLI app

Phase 3 turns the parse-and-analyse pattern from Phase 2 into an
interactive command-line application. The domain switches to World of
Warcraft DPS logs.

## Files

| File | What it does |
|------|--------------|
| `logs.txt` | Data file — one run per line: `player_name,class,role,dps`. |
| `app.py` | Loads the logs and runs an interactive menu loop. |

## Data format

```
Shaun,Evoker,DPS,12500
John,Mage,DPS,14200
Shaun,Evoker,DPS,13200
Anna,Priest,Healer,9800
Alex,Warrior,Tank,10300
```

## Menu options

```
1. Show all logs
2. Show runs by class
3. Show highest DPS by class
4. Show average DPS by class
5. Exit
```

## Functions in `app.py`

| Function | Purpose |
|----------|---------|
| `load_log()` | Read `logs.txt`, return a list of dicts. |
| `get_runs_by_class(comps, class_name)` | All runs for a given class (case-insensitive). |
| `highest_dps_by_class(comps)` | Highest-DPS run for each class. |
| `average_dps_by_class(comps)` | Average DPS for each class. |
| `main()` | The CLI menu loop, with input validation. |

## Key lesson

Same load → transform → output pipeline as Phase 2, but now wrapped in a
`main()` loop with user input and validation — moving from "a script that
runs once" to "a program a user interacts with".

## Running

```bash
cd phase3
python3 app.py
```

> Note: run it from inside `phase3/` so `logs.txt` is found.
