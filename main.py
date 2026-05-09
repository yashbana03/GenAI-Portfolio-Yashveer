import os 
from pathlib import Path
if not os.path.exists("data"):
 os.mkdir("data")

for i in range(1,101):
    if not os.path.exists(f"data/tutorial{i}"):
     os.mkdir(f"data/tutorial{i}")
Path("oslist.py").touch()
