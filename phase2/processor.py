def load_records():
    record_list = []   # ← create list ONCE

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
print(records)