def load_records():
    with open("records.txt") as f:
        lines = f.readlines()
        lines = lines[0]
        print(lines)
        print(lines.strip().split(","))
        
load_records()