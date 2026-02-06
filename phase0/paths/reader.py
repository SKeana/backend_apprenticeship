import os

Base_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(Base_DIR, "data.txt")


with open("data.txt") as f:
    print(f.read())