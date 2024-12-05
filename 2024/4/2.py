#!/usr/bin/env python3

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [line.strip() for line in lines]

# Pad so don't have to check for bounds
for y, line in enumerate(lines):
    lines[y] = f".{line}."
added_lines = ['.' * len(lines[0])]
lines = added_lines + lines + added_lines

count = 0
for y in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-1):
        if lines[y][x] == 'A':
            cx1 = lines[y-1][x-1], lines[y+1][x+1]
            cx2 = lines[y+1][x-1], lines[y-1][x+1]
            if ['M', 'S'] == sorted(cx1) and ['M', 'S'] == sorted(cx2):
                count += 1
print(count)
