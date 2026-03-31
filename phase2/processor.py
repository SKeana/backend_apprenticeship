def load_records():
    with open("records.txt") as f:
        lines = f.readlines()
        print(lines)

load_records()