import re
from collections import namedtuple
from functools import cache
    
Range = namedtuple('Range', ['dest', 'src', 'len'])

mappings: dict[str, list[Range]] = {}

with open('input.txt', 'r') as f:
    for line in [x.strip() for x in f.readlines()]:
        
        if line.startswith('seeds:'):
            p1_seeds = [int(x) for x in re.findall(r'(\d+)', line[6:])]
            p2_seeds = [(int(x), int(y)) for (x, y) in re.findall(r'(?:(\d+) (\d+))', line[6:])]
            
        elif line.endswith(':'):
            m = re.match(r'(.*) map:', line)
            if m:
                current_mapping = m.group(1)
                mappings[current_mapping] = []
                
        else:
            if m := re.match(r'(\d+) (\d+) (\d+)', line):
                new_range = Range(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                mappings[current_mapping].append(new_range)
                
for mapping in mappings:
    print(mapping, mappings[mapping])

def find_output_for_input(ranges, input):
    for current_range in ranges:
        if input >= current_range.src and input < current_range.src + current_range.len:
            print(f'{input} in range {current_range.src} - {current_range.src + current_range.len} -> output {current_range.dest + (input - current_range.src)}')
            return current_range.dest + (input - current_range.src)
    return input

def find_location(seed):
    input = seed
    for mapping, values in mappings.items():
        print(f'{mapping}:', end='')        
        input = find_output_for_input(values, input)
    return input

# Part 1
locations = []
for seed in p1_seeds:
    locations.append(find_location(seed))
print(f'Part 1: Location {min(locations)}')

# Part 2
mins = []
for seed_range in p2_seeds:
    print(seed_range)
    locations = [find_location(seed) for seed in range(seed_range[0], seed_range[0] + seed_range[1])]
    print(f'Found locations {locations}')
    mins.append(min(locations))
print(f'Part 2: Location {min(mins)}')