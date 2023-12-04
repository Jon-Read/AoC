# The basic approach here is to treat the schematic as a two-dimensional array.
# Find each number, create a bounding box that includes array members immediately
# surrounding it, and check for a symbol inside that box.

# We pad the array so that we don't have to deal with cases where the numbers
# are positioned at the "edge" of the array.

import re

total = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    # Pad lines at each end to avoid having to deal with literal edge cases
    lines = [f'.{x.strip()}.' for x in lines]
    line_len = len(lines[0])
    
    # Add some "blank" lines for the same reason
    lines.insert(0, '.' * line_len)
    lines.append('.' * line_len)
    
    for line_index in range(1, len(lines) - 1):
        line = lines[line_index]
        m = re.finditer(r'(\d+)', line)
        for match in m:
            # For each number found, record the horizontal start/end of
            # out virtual bounding box
            start = match.start() - 1
            end = match.end() + 1
            
            # The bounding box is the current line, plus the ones before and after
            for check_line_index in range(line_index - 1, line_index + 2):
                # Get the correct chunk of the line
                chunk = lines[check_line_index][start:end]
                if [x for x in chunk if not x.isdecimal() and x != '.']:
                    # Found a symbol, get number and add to total
                    total += int(match.group(1))
                    break
                    
print(f'TOTAL: {total}')
                    
            
        