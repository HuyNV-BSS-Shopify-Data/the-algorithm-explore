from os import walk
import os
import pandas as pd

readmes = []

def first_title(path):
    with open(path, "r") as f:
        t = f.read().split("\n")
    for line in t:
        if line.startswith("#"):
            return line

for path, folders, files in walk("the-algorithm"):
    for f in files:
        if f.endswith("README.md"):
            project_path=os.path.join( os.path.abspath(path), f )
            print(project_path)
            readmes.append({
                "path":project_path[ project_path.find("/the-algorithm/"): ],
                "size":os.path.getsize(project_path),
                "first_title": first_title(project_path)
            })
            
pd.DataFrame(readmes).to_csv("readmes/readmes.csv")
            