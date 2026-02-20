What directory am I being run from?
backend-appticeship  
Where does this file live?
phase 1 
What files are in the current directory?
data2.txt, probe.py and reflection. 
----
I didn't read the qestion wrong.
What directory am I being run from?
" current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship"
Where does this file live?
 " files current location:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1/probe.py
What files are in the current directory?
Python executable:
/usr/bin/python3

 current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship

 All files in directory:
probe.py
reflection.md
data2.txt

---
from root (backend_appnticeship)
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ pwd
/home/skean/codingProjects/pythonProjects/backend_apprenticeship
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ ls
phase0  phase1
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ python3 phase1/probe.py
Python executable:
/usr/bin/python3

 current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship

 All files in directory:
probe.py
reflection.md
data2.txt

from phase1 
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ pwd
/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ ls
data2.txt  probe.py  reflection.md
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ python3 phase1/probe.py
python3: can't open file '/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1/phase1/probe.py': [Errno 2] No such file or directory

---

skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ python3 probe.py
Python executable:
/usr/bin/python3

 current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1

 All files in directory:
Traceback (most recent call last):
  File "/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1/probe.py", line 14, in <module>
    for item in phase1_path.iterdir():
  File "/usr/lib/python3.12/pathlib.py", line 1058, in iterdir
    for name in os.listdir(self):
                ^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/home/skean/codingProjects/pythonProjects/backend_apprenticeship/phase1/phase1'
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship/phase1$ cd ..
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ python3 phase1/probe.py
Python executable:
/usr/bin/python3

 current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship

 All files in directory:
probe.py
reflection.md
data2.txt
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ 

also can you look at the code in probe.py inside of phase1 as I want to make sure i did it right:
import os
import sys
from pathlib import Path

print("Python executable:")
print(sys.executable)

print("\n current working directory:")
print(os.getcwd())

print("\n All files in directory:")
phase1_path = Path.cwd() / "phase1"

for item in phase1_path.iterdir():
    if item.is_file():
        print(item.name)

---
here is the output after making the changes in probe.py
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ python3 probe.py
python3: can't open file '/home/skean/codingProjects/pythonProjects/backend_apprenticeship/probe.py': [Errno 2] No such file or directory
skean@Shaun:~/codingProjects/pythonProjects/backend_apprenticeship$ python3 phase1/probe.py
Python executable:
/usr/bin/python3

 current working directory:
/home/skean/codingProjects/pythonProjects/backend_apprenticeship

All files in current working directory: