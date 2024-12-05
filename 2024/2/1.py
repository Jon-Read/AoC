#!/usr/bin/env python3
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

file = "example1.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [line.strip() for line in lines]

count = 0
for line in lines:
    values = [int(x) for x in line.split(' ')]
    diffs = [values[x] - values[x+1] for x in range(len(values)-1)]
    
    if len([x for x in diffs if abs(x) < 1 or abs(x) > 3]) > 0:
        continue
    
    if len([x for x in diffs if x < 0]) > 1 and len([x for x in diffs if x > 0]) > 1:
        continue
    
    count += 1
        
print(count)