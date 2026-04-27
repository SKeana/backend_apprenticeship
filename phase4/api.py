from fastapi import FastAPI, HTTPException

app = FastAPI()

def load_log() -> list:
    comps = []

    with open("logs.txt") as f:
        for line in f:
            roles = line.strip().split(",")

            comp = {
                "player_name": roles[0],
                "class": roles[1],
                "role": roles[2],
                "dps": int(roles[3])
            }

            comps.append(comp)

    return comps

comps = load_log()


def get_runs_by_class(comps, class_name):
    runs = []

    for comp in comps:
        if comp["class"].lower() == class_name.lower():
            runs.append(comp)

    return runs


def highest_dps_by_class(comps):
    highest = {}

    for comp in comps:
        class_name = comp["class"]

        if class_name not in highest or comp["dps"] > highest[class_name]["dps"]:
            highest[class_name] = comp

    return highest


def average_dps_by_class(comps):
    dps_sum = {}
    count = {}

    for comp in comps:
        class_name = comp["class"]

        if class_name not in dps_sum:
            dps_sum[class_name] = 0
            count[class_name] = 0

        dps_sum[class_name] += comp["dps"]
        count[class_name] += 1

    return {
        class_name: dps_sum[class_name] / count[class_name]
        for class_name in dps_sum
    }


# -------------------------
# API ENDPOINTS
# -------------------------

@app.get("/")
def home():
    return {"message": "WoW Log API is running"}


@app.get("/logs")
def show_logs():
    return comps


@app.get("/class/{class_name}")
def show_runs_by_class(class_name: str):
    runs = get_runs_by_class(comps, class_name)

    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    return runs


@app.get("/highest-dps")
def show_highest_dps():
    return highest_dps_by_class(comps)


@app.get("/average-dps")
def show_average_dps():
    return average_dps_by_class(comps)


@app.get("/class/{class_name}/highest")
def show_highest_dps_for_class(class_name: str):
    runs = get_runs_by_class(comps, class_name)

    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    highest = runs[0]

    for run in runs:
        if run["dps"] > highest["dps"]:
            highest = run

    return highest


@app.get("/class/{class_name}/average")
def show_average_dps_for_class(class_name: str):
    runs = get_runs_by_class(comps, class_name)

    if not runs:
        raise HTTPException(status_code=404, detail="Class not found")

    dps_sum = sum(run["dps"] for run in runs)
    average = dps_sum / len(runs)

    return {
        "class": class_name,
        "average_dps": average
    }