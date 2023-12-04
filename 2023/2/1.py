import re

# We have this number of each cube
NUM_RED = 12
NUM_BLUE = 14
NUM_GREEN = 13

total: int = 0

with open("input.txt", "r") as f:
    for line in f:
        m = re.match(r"Game (\d+): (.*)", line)
        if m:
            game_number = int(m.group(1))
            draws_str = m.group(2)

        draws_list = draws_str.split(";")

        is_possible = True
        for draw in draws_list:
            red_match = re.search(r"(\d+) red", draw)
            blue_match = re.search(r"(\d+) blue", draw)
            green_match = re.search(r"(\d+) green", draw)

            red_count = int(red_match.group(1)) if red_match else 0
            blue_count = int(blue_match.group(1)) if blue_match else 0
            green_count = int(green_match.group(1)) if green_match else 0

            if red_count > NUM_RED or blue_count > NUM_BLUE or green_count > NUM_GREEN:
                is_possible = False

            print(f"  - {red_count}, {blue_count}, {green_count}, {is_possible}")

        if is_possible:
            total += game_number
            print("Is possible.")

print("Possible games total:", total)
