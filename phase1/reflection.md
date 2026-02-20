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

---
What happens was before the changes that were made in probe.py, the code was trying to fine phase1/phase1 and as ther wasn't a directory inside of phas1 call phase1 there was an error but after the changes to probe.py it is looking for the files in the path with cwd then show the files inside of that directory
`
Yes.

That is correct.

Now I’m going to tighten your explanation into backend precision:

Earlier, the code did:

Path.cwd() / "phase1"

So when you were already inside phase1, the program constructed:

/backend_apprenticeship/phase1/phase1

That directory does not exist.

The bug was not Python.
The bug was assuming the current working directory was always the project root.

After the change, you removed the assumption and asked the system directly:

“What directory am I currently in?”

That is stable logic.

Phase 1 Probe Status

You now understand:

Shell resolves script path.

Python resolves file paths inside the script.

Path.cwd() depends on execution location.

Path(__file__).parent depends on file location.

Hardcoding folder names creates fragile code.

That is real foundational backend knowledge.

You’re not just typing Python anymore.
You’re reasoning about execution environments.

That shift matters.

Quick Assessment

You handled:

Confusion

Frustration

A real filesystem bug

A logic assumption bug

Silent output

Path resolution errors

And you didn’t quit.

That’s what I’m watching for.

Next Phase: Functions (where backend thinking actually starts)

Up until now you’ve been writing scripts.

Now we move to:

Inputs → transformation → outputs

Predictable behavior

Separation of concerns

You are going to build something small but structured.

Create:

phase1/functions_probe.py

The task:

Write a function:

describe_environment()

When called, it should:

Return (not print) a dictionary containing:

python_executable

current_working_directory

script_directory

files_in_current_directory (list)

Then at the bottom of the file:

Call the function

Print the returned dictionary cleanly

No hints beyond that.

This is the first real backend-style exercise.

When done, paste:

The function code

The output

We’re stepping up now.
`