#!/usr/bin/env python3

from functools import cmp_to_key

file = "input.txt"

# Input file parsing
with open(file, "r") as f:
	text = f.read()	
sections = text.split("\n\n")
rules_input = sections[0].splitlines()
page_lists = [x.split(",") for x in sections[1].splitlines()]
rules = [(x.split('|')[0], x.split("|")[1]) for x in rules_input]

def key_fn(a, b) -> int:
    for before, after in rules:
        if a == before and b == after:
            return -1
    return 1

total = 0    
for pages in page_lists:
    new_pages = sorted(pages, key=cmp_to_key(key_fn))
    if pages != new_pages:
        # print(f"{pages} --> {new_pages}")
        total += int(new_pages[len(new_pages)//2])
    
print(f"{total=}")