#!/usr/bin/env python3

file = "input.txt"

with open(file, "r") as f:
	text = f.read()	
# lines = [line.strip() for line in lines]

sections = text.split("\n\n")
rules_input = sections[0].splitlines()
page_lists = [x.split(",") for x in sections[1].splitlines()]

rules = [(x.split('|')[0], x.split("|")[1]) for x in rules_input]

total = 0
for pages in page_lists:
    for idx, page in enumerate(pages):
        matching = [r[1] for r in rules if r[0] == page and r[1] in pages]
        following_pages = pages[idx+1:]
        if sorted(matching) != sorted(following_pages):
            break
    else:
        total += int(pages[len(pages)//2])

print(f"Total: {total}")