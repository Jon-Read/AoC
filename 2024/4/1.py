#!/usr/bin/env python3

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [line.strip() for line in lines]

# Pad so don't have to check for bounds
for y, line in enumerate(lines):
    lines[y] = f"...{line}..."
added_lines = ['.' * len(lines[0])] * 3
lines = added_lines + lines + added_lines

def subscan(x, y, dx, dy, word):
    if lines[y+dy][x+dx] == word[0]:
        # print(f"got {word[0]}")
        if len(word) == 1:
            # print("match!")
            return 1
        else:
            return subscan(x+dx, y+dy, dx, dy, word[1:])
    return 0

def scan(x, y):
    word = "XMAS"
    
    count = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]:
        count += subscan(x, y, dx, dy, word)
        
    if count > 0:
        print(f"got {count} matches at {x, y}")
    return count
            
count = 0
for y in range(2, len(lines) - 2):
    for x in range(2, len(lines[0]) - 2):
        count += scan(x, y)
print(count)
