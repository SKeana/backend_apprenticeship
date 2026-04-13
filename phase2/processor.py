def load_records():
    record_list = []

    with open("records.txt") as f:
        lines = f.readlines()

        for line in lines:
            parts = line.strip().split(",")

            record = {
                "name": parts[0],
                "age": int(parts[1]),
                "role": parts[2]
            }
            record_list.append(record)

    return record_list


def group_by_role(records):
    grouped = {}

    for record in records:
        role = record["role"]

        if role not in grouped:
            grouped[role] = []

        grouped[role].append(record)
    return grouped

def count_by_role(records):
    counts = {}

    for record in records:
        role = record["role"]

        if role not in counts:
            counts[role] = 0

        counts[role] += 1

    return counts


# Run everything
records = load_records()
grouped_records = group_by_role(records)
role_counts = count_by_role(records)


print(grouped_records)
print("----")
print(role_counts) 