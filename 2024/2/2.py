#!/usr/bin/env python3
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [line.strip() for line in lines]

def is_safe(values: list) -> bool:
    diffs = [values[x] - values[x+1] for x in range(len(values)-1)]
    
    if len([x for x in diffs if x < 0]) > 0 and len([x for x in diffs if x > 0]) > 0:
        # print(f'{line} {diffs} unsafe, rule 1')
        return False

    if len([x for x in diffs if abs(x) < 1 or abs(x) > 3]) > 0:
        # print(f'{line} {diffs} unsafe, rule 2')
        return False
    
    # print(f'{line} {diffs} is safe')
    return True

count = 0
for line in lines:
    values = [int(x) for x in line.split(' ')]
    
    if is_safe(values):
        count += 1
    else:
        for n in range(len(values)):
            temp_values = values[0:n] + values[n+1:]
            if is_safe(temp_values):
                print(f'{values} -> {temp_values} is safe')
                count += 1
                break
                    
print(count)