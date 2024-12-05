#!/usr/bin/env python3

import re

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [x.strip() for x in lines]

total = 0
for line in lines:
	matches = re.findall(r"mul\((\d+),(\d+)\)", line)
	vals = [int(x)*int(y) for x, y in matches]
	total += sum(vals)
 
print(total)