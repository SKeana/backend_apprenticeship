def load_records():
    with open("records.txt") as f:
        lines = f.readlines()
        line = lines[0]

        parts = line.strip().split(",")

        record = {
            "name": parts[0],
            "age": int(parts[1]),
            "role": parts[2]
        }

        print(record)

load_records()