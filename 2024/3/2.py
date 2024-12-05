#!/usr/bin/env python3

import re

file = "input.txt"

with open(file, "r") as f:
	lines = f.readlines()	
lines = [x.strip() for x in lines]

enable = True
total = 0
for line in lines:
	matches = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))", line)
 
	for match in matches:
		if match[0] == "do()":
			enable = True
		elif match[0] == "don't()":
			enable = False
		elif enable:
			total += int(match[1]) * int(match[2])
 
print(total)