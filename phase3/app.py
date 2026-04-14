def load_log() -> list:
    comps = []

    with open("logs.txt") as f:
        lines = f.readlines()
    
    with open("logs.txt", "r") as f:
        line = f.readline()

        for line in lines:
            roles = line.strip().split(",")

            group_comp = {
                "player name": roles[0],
                "class": roles[1],
                "role": roles[2],
                "dps": int(roles[3])
            }
            comps.append(group_comp)
    return comps

comps = load_log()
print(comps)