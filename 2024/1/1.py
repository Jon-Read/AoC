#!/usr/bin/env python3

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [line.strip() for line in lines]

lists = [[int(v) for v in n.split("   ")] for n in lines]
lists = zip(sorted([v[0] for v in lists]), sorted([v[1] for v in lists]))
diffs = [abs(b - a) for a, b in lists]

print(sum(diffs))
