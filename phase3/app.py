def load_log() -> list:
    comps = []

    with open("logs.txt") as f:
        lines = f.readlines()

        for line in lines:
            info = line.strip().split(",")

            group_comp = {
                "player_name": info[0],
                "class": info[1],
                "role": info[2],
                "dps": int(info[3])
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

    average_dps = {class_name: dps_sum[class_name] / count[class_name] for class_name in dps_sum}
    return average_dps

comps = load_log()
for comp in comps:
    print(comp)
print("---")
runs = get_runs_by_class(comps, "Evoker")
for run in runs:
    print(run)
print("---")
print("Highest DPS by class:")
highest_dps = highest_dps_by_class(comps)
for class_name, dps in highest_dps.items():
    print(f"{class_name}: {dps}")
print("---")
print("Average DPS by class:")
average_dps = average_dps_by_class(comps)
for class_name, avg_dps in average_dps.items():
    print(f"{class_name}: {avg_dps:.2f}")
print("---")