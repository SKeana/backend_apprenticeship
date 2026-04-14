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
        if comp["class"] == class_name:
            runs.append(comp)

    return runs


comps = load_log()
for comp in comps:
    print(comp)
print("---")
runs = get_runs_by_class(comps, "Evoker")
for run in runs:
    print(run)
print("---")