# Here we need to work out the fewest number of each RGB cubes
# we need to make the game possible.

import re

total = 0

with open("input.txt", "r") as f:
    for line in f:
        m = re.match(r"Game (\d+): (.*)", line)
        draws_str = m.group(2)

        red_max = 0
        blue_max = 0
        green_max = 0
        
        # Iterate through each draw in this game
        draws_list = draws_str.split(";")
        for draw in draws_list:
            red_match = re.search(r"(\d+) red", draw)
            blue_match = re.search(r"(\d+) blue", draw)
            green_match = re.search(r"(\d+) green", draw)

            # Get cube counts for this draw
            red_count = int(red_match.group(1)) if red_match else 0
            blue_count = int(blue_match.group(1)) if blue_match else 0
            green_count = int(green_match.group(1)) if green_match else 0

            # Keep track of the number of each cube we need so far
            red_max = max(red_max, red_count)
            blue_max = max(blue_max, blue_count)
            green_max = max(green_max, green_count)

        # Calculate the "power" as per the rules and maintain the total
        power = red_max * blue_max * green_max
        total += power

print("Power total:", total)
