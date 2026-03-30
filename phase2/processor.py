from pathlib import Path

def filepath():
    with open("records.txt") as f:
        lines = f.readlines()
        print(f.readline)