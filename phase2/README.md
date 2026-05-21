# Phase 2 — Parsing structured data

The first phase that works with real data. `records.txt` holds CSV-style
rows; `processor.py` parses them into a list of dictionaries and runs
grouping, filtering, and aggregation against that list.

## Files

| File | What it does |
|------|--------------|
| `records.txt` | Data file — one record per line: `name,age,role`. |
| `processor.py` | Loads the file and runs all the analysis functions. |

## Data format

```
Alice,29,Engineer
Bob,34,Designer
Charlie,22,Engineer
Diana,40,Manager
Eve,29,Designer
```

## Functions in `processor.py`

| Function | Purpose |
|----------|---------|
| `load_records()` | Read `records.txt`, return a list of dicts. |
| `group_by_role(records)` | Group records into lists keyed by `role`. |
| `count_by_role(records)` | Count how many records each role has. |
| `filter_by_age(records, min_age)` | Keep only records at or above `min_age`. |
| `group_filter_by_role(records, min_age)` | Filter by age, then group by role. |
| `oldest_per_role(records)` | Find the oldest record in each role. |

## Key lesson

Turning flat text into structured data (`list[dict]`) is the foundation of
every backend task that follows — Phase 3 and Phase 4 reuse exactly this
load → transform → output pattern.

## Running

```bash
cd phase2
python3 processor.py
```

> Note: `processor.py` opens `records.txt` by relative path, so run it from
> inside the `phase2/` folder.
