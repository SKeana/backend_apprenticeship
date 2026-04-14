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

def filter_by_age(records, min_age):
    filtered = []

    for record in records:
        if record["age"] >= min_age:
            filtered.append(record)

    return filtered

def group_filter_by_role(records, min_age):
    grouped = {}

    for record in records:
        if record["age"] >= min_age:
            role = record["role"]

            if role not in grouped:
                grouped[role] = []

            grouped[role].append(record)

    return grouped

def oldest_per_role(records):
    oldest = {}

    for record in records:
        role = record["role"]

        if role not in oldest or record["age"] > oldest[role]["age"]:
            oldest[role] = record

    return oldest

# Run everything
records = load_records()
grouped_records = group_by_role(records)
role_counts = count_by_role(records)


print(grouped_records)
print("----")
print(role_counts) 
print("----")
print(filter_by_age(records, 30))
print("----")
print(group_filter_by_role(records, 30))
print("----")
print(oldest_per_role(records))