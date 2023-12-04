# OK, so we have to flip the approach from 1.py so instead of finding
# the numbers we find the multiplication symbol.

# Instead of using a bounding box here, we'll look for numbers in the
# surrounding lines and see if they're adjacent to the operator.  If
# so, multiply and add as per the rules.

import re

total = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    # Pad lines to avoid having to deal with literal edge cases
    lines = [f'.{x.strip()}.' for x in lines]
    line_len = len(lines[0])
    
    # Add some "blank" lines for the same reason
    lines.insert(0, '.' * line_len)
    lines.append('.' * line_len)
    
    for line_index in range(1, len(lines) - 1):
        line = lines[line_index]
        # find all '*' values
        m = re.finditer(r'(\*)', line)
        for match in m:
            surrounding_values = []
            pos = match.start()
            
            # check for surrounding values
            for check_line_index in range(line_index - 1, line_index + 2):
                value_matches = re.finditer(r'(\d+)', lines[check_line_index])
                for value_match in value_matches:
                    if pos > (value_match.start() - 2) and pos < (value_match.end() + 1):
                        surrounding_values.append(int(value_match.group(1)))
                    
            # If there are two surrounding values, add as per the rules. Otherwise ignore.
            if len(surrounding_values) == 2:
                total += (int(surrounding_values[0]) * int(surrounding_values[1]))
                    
print(f'TOTAL: {total}')
                    
            
        