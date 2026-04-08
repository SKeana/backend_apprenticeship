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


# Run everything
records = load_records()
grouped_records = group_by_role(records)

print(grouped_records) 