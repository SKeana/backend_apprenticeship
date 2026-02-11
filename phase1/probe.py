import os

dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, "data2.txt")

with open(data_path) as f:
    print(f.read())