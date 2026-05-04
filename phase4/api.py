from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pathlib import Path

app = FastAPI()


# -------------------------
# DATA LOADING
# -------------------------

def load_log() -> list:
    comps = []

    file_path = Path(__file__).parent / "logs.txt"

    with open(file_path) as f:
        for line in f:
            roles = line.strip().split(",")

            comp = {
                "player_name": roles[0],
                "class_name": roles[1],
                "role": roles[2],
                "dps": int(roles[3])
            }

            comps.append(comp)

    return comps


# Load once (shared data)
comps = load_log()


# -------------------------
# LOGIC FUNCTIONS
# -------------------------

def get_runs_by_class(comps, class_name):
    return [
        comp for comp in comps
        if comp["class_name"].lower() == class_name.lower()
    ]


def get_runs_by_class_filtered(comps, class_name, min_dps=None):
    runs = get_runs_by_class(comps, class_name)

    # 1. Check class exists
    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    # 2. Apply filter
    if min_dps is not None:
        runs = [run for run in runs if run["dps"] >= min_dps]

        if not runs:
            raise HTTPException(status_code=404, detail="No runs match the filter")

    return {
        "count": len(runs),
        "results": runs
    }


def highest_dps_by_class(comps):
    highest = {}

    for comp in comps:
        class_name = comp["class_name"]

        if class_name not in highest or comp["dps"] > highest[class_name]["dps"]:
            highest[class_name] = comp

    return highest


def average_dps_by_class(comps):
    dps_sum = {}
    count = {}

    for comp in comps:
        class_name = comp["class_name"]

        if class_name not in dps_sum:
            dps_sum[class_name] = 0
            count[class_name] = 0

        dps_sum[class_name] += comp["dps"]
        count[class_name] += 1

    return {
        class_name: dps_sum[class_name] / count[class_name]
        for class_name in dps_sum
    }

#-------------------------
# MODELS 
#-------------------------

class Run(BaseModel):
    player_name: str
    class_name: str
    role: str
    dps: int
class RunListResponse(BaseModel):
    count: int
    results: List[Run]

class AverageResponse(BaseModel):
    class_name: str
    average_dps: float

# -------------------------
# API ENDPOINTS
# -------------------------

@app.get("/")
def home():
    return {"message": "WoW Log API is running"}


@app.get("/logs")
def show_logs():
    return {
        "count": len(comps),
        "results": comps
    }


@app.get("/class/{class_name}", response_model=RunListResponse)
def show_runs_by_class(class_name: str, min_dps: int = None):
    return get_runs_by_class_filtered(comps, class_name, min_dps)


@app.get("/highest-dps")
def show_highest_dps():
    return highest_dps_by_class(comps)


@app.get("/average-dps")
def show_average_dps():
    return average_dps_by_class(comps)


@app.get("/class/{class_name}/highest", response_model=Run)
def show_highest_dps_for_class(class_name: str):
    runs = get_runs_by_class(comps, class_name)

    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    highest = runs[0]

    for run in runs:
        if run["dps"] > highest["dps"]:
            highest = run

    return highest


@app.get("/class/{class_name}/average", response_model=AverageResponse)
def show_average_dps_for_class(class_name: str):
    runs = get_runs_by_class(comps, class_name)

    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    avg = sum(run["dps"] for run in runs) / len(runs)

    return {
        "class_name": class_name,
        "average_dps": avg
    }