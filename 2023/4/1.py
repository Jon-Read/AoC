import re

with open('input.txt', 'r') as f:

    total: int = 0    
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        
        m = re.match(r'Card +(\d+): ([\d ]+) \| ([\d ]+)', line)
        if m:
            card = m.group(1)
            
            winning = [int(x) for x in m.group(2).split()]
            mine = [int(x) for x in m.group(3).split()]
            
            intersection = list(set(winning) & set(mine))
            
            if len(intersection):
                total += pow(2,len(intersection)-1)

print(total)