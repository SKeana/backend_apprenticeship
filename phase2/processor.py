def load_records():
    with open("records.txt") as f:
        lines = f.readlines()
        lines = lines[0]
        #print(lines)
        parts = lines.strip().split(",") 
        print(parts[0])
        print(parts[1])
        print(parts[2])

load_records()