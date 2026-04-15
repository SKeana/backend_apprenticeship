def load_log() -> list:
    comps = []

    with open("logs.txt") as f:
        lines = f.readlines()

        for line in lines:
            roles = line.strip().split(",")

            group_comp = {
                "player_name": roles[0],
                "class": roles[1],
                "role": roles[2],
                "dps": int(roles[3])
            }

            comps.append(group_comp)

    return comps

def get_runs_by_class(comps, class_name):
    runs = []

    for comp in comps:
        if comp["class"].lower() == class_name.lower():
            runs.append(comp)

    return runs

def highest_dps_by_class(comps):
    highest_dps = {}

    for comp in comps:
        class_name = comp["class"]
        dps = comp["dps"]

        if class_name not in highest_dps or dps > highest_dps[class_name]:
            highest_dps[class_name] = dps

    return highest_dps

comps = load_log()
for comp in comps:
    print(comp)
print("---")
runs = get_runs_by_class(comps, "Evoker")
for run in runs:
    print(run)
print("---")
highest_dps = highest_dps_by_class(comps)
for class_name, dps in highest_dps.items():
    print(f"{class_name}: {dps}")
print("---")