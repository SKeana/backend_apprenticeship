import os

Base_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(Base_DIR, "data.txt")


with open(DATA_PATH) as f:
    print(f.read())
    