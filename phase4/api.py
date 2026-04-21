from fastapi import FastAPI

app = FastAPI()


def load_log() -> list:
    comps = []

    with open("logs.txt") as f:
        lines = f.readlines()

        for line in lines:
            roles = line.strip().split(",")

            comp = {
                "player_name": roles[0],
                "class": roles[1],
                "role": roles[2],
                "dps": int(roles[3])
            }

            comps.append(comp)

    return comps


def get_runs_by_class(comps, class_name):
    runs = []

    for comp in comps:
        if comp["class"].lower() == class_name.lower():
            runs.append(comp)

    return runs

def average_dps_by_class(comps):
    dps_sum = {}
    count = {}

    for comp in comps:
        class_name = comp["class"]
        dps = comp["dps"]

        if class_name not in dps_sum:
            dps_sum[class_name] = 0
            count[class_name] = 0

        dps_sum[class_name] += dps
        count[class_name] += 1

    average_dps = {
        class_name: dps_sum[class_name] / count[class_name]
        for class_name in dps_sum
    }

    return average_dps

def highest_dps_by_class(comps):
    highest_dps = {}

    for comp in comps:
        class_name = comp["class"]

        if class_name not in highest_dps or comp["dps"] > highest_dps[class_name]["dps"]:
            highest_dps[class_name] = comp
    return highest_dps


@app.get("/")
def home():
    return {"message": "WoW Log API is running"}


@app.get("/logs")
def show_logs():
    return load_log()


@app.get("/class/{class_name}")
def show_runs_by_class(class_name: str):
    comps = load_log()
    return get_runs_by_class(comps, class_name)


@app.get("/highest-dps")
def show_highest_dps():
    comps = load_log()
    return highest_dps_by_class(comps)


@app.get("/average-dps")
def show_average_dps():
    comps = load_log()
    return average_dps_by_class(comps)

@app.get("/class/{class_name}/highest")
def show_highest_dps_by_class(class_name: str):
    comps = load_log()
    highest_dps = highest_dps_by_class(comps)
    return highest_dps.get(class_name, {"message": "Class not found"})