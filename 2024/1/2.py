#!/usr/bin/env python3

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()
lines = [line.strip() for line in lines]

values = [int(v) for v in [n.split("   ")[0] for n in lines]]
occurrences = [int(v) for v in [n.split("   ")[1] for n in lines]]

total = 0
for value in values:
	count = occurrences.count(value)
	total += value * count
	
print(total)