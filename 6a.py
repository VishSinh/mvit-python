import os.path
import sys

fname = input("Enter the filename: ")

if not os.path.isfile(fname):
    print(f"File {fname} doesn't exist")
    sys.exit(0)

with open(fname, "r") as infile:
    lines = infile.readlines()

for i, line in enumerate(lines[:3]):
    print(f"{i+1} : {line.strip()}")

word = input("Enter a word: ")
count = sum(line.count(word) for line in lines)

print(f"The word '{word}' appears {count} times in the file")
