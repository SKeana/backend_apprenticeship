def load_records():
    record_list = []   # ← create list ONCE
    role_list = []

    with open("records.txt") as f:
        lines = f.readlines()

        for line in lines:
            parts = line.strip().split(",")

            record = {
                "name": parts[0],
                "age": int(parts[1]),
                "role": parts[2]
            }
            record_list.append(record)  # ← add to same list

    return record_list   # ← give the result back

records = load_records()
#print(records)

def group_by_role(records):
    grouped = {}

    for record in records:
        role = record["role"]
        if role not in grouped:
            grouped[role] = []
            print(grouped)


group_by_role(records)