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


def highest_dps_by_class(comps):
    highest_dps = {}

    for comp in comps:
        class_name = comp["class"]

        if class_name not in highest_dps or comp["dps"] > highest_dps[class_name]["dps"]:
            highest_dps[class_name] = comp

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

    average_dps = {
        class_name: dps_sum[class_name] / count[class_name]
        for class_name in dps_sum
    }

    return average_dps


# -------------------------
# MAIN PROGRAM (CLI)
# -------------------------

def main():
    comps = load_log()

    while True:
        choice = input(
            "\n1. Show all logs\n"
            "2. Show runs by class\n"
            "3. Show highest DPS by class\n"
            "4. Show average DPS by class\n"
            "5. Exit\n"
            "Choose an option: "
        )

        if choice == "1":
            for comp in comps:
                print(comp)

        elif choice == "2":
            while True:
                class_name = input("Enter class name: ")

                if not class_name:
                    print("Class name cannot be empty.")
                    continue

                runs = get_runs_by_class(comps, class_name)

                if not runs:
                    print("There is no class with that name in the logs. Try again.")
                else:
                    for run in runs:
                        print(run)
                    break

        elif choice == "3":
            highest = highest_dps_by_class(comps)
            print("\nHighest DPS by class:")
            for class_name, comp in highest.items():
                print(f"{class_name}: {comp['player_name']} - {comp['dps']}")

        elif choice == "4":
            averages = average_dps_by_class(comps)
            print("\nAverage DPS by class:")
            for class_name, avg in averages.items():
                print(f"{class_name}: {avg:.2f}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


# Run the program
if __name__ == "__main__":
    main()