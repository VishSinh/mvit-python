import re
with open('5b.txt', 'r') as f:
    for line in f:
        if re.compile(r'\+\d{12}').match(line) or re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$').match(line):
            print(line, end='')
