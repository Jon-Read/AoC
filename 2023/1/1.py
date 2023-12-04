import re

replacements = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

# Regex finds any overlapping text digits
RE = r"(?=(one|two|three|four|five|six|seven|eight|nine))"


def repl(matchobj):
    """Callback from re.sub() to replace string matches with
    digit from replacement map"""
    value = replacements[matchobj.group(1)]
    return value


with open("input.txt", "r") as f:
    total: int = 0

    for line in f:
        replaced_line = re.sub(RE, repl, line)
        m = re.findall(r"\d", replaced_line)
        total += int(m[0] + m[-1])

print(total)
