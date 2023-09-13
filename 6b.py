import os
import sys
from pathlib import Path
import zipfile

dir_name = input("Enter the directory name that you want to backup: ")

if not os.path.isdir(dir_name):
    print(f"Directory {dir_name} doesn't exist")
    sys.exit(0)

with zipfile.ZipFile("myZip.zip", "w") as archive:
    for file_path in Path(dir_name).rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(dir_name))

print(f"Archive 'myZip.zip' {'created successfully' if os.path.isfile('myZip.zip') else 'failed to create'}")
