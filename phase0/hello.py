import sys
print(sys.version)

import os

results = []
testdir = "C:\Test"
for folder in testdir:
  for f in os.listdir(folder):
    if f.endswith('.pdf'):
        results.append(f)

print (results)


file_name = __file__
print(f'This file is located at: {file_name}')