import re

raw_input = open("./inputs/day3.txt", "r").read()

print(raw_input)

mult_pair_regex = r"mul\(\d?\d?\d?,\d?\d?\d?\)"

matches = re.finditer(mult_pair_regex, raw_input, re.MULTILINE)

def mult_pair(match, do = True):
    left = match.group().split("(")[1].split(",")[0]
    right = match.group().split(",")[1].split(")")[0]
    return int(left) * int(right) * (1 if do else 0)

# Part 1
print("Day 3 Part 1:\n", sum([mult_pair(match,True) for match in matches]))

do_regex = r"do\(\)"

dont_regex = r"don't\(\)"

do_matches = re.finditer(do_regex, raw_input, re.MULTILINE)

dont_matches = re.finditer(dont_regex, raw_input, re.MULTILINE)

do_positions = [0] + [match.start() for match in do_matches] # starts as doing

dont_positions = [-1] + [match.start() for match in dont_matches] # -1 to avoid index out of bounds below

def do_or_dont(match_start_position, do_positions, dont_positions):
    last_do_before_match_start_position = [do for do in do_positions if do < match_start_position][-1]
    last_dont_before_match_start_position = [dont for dont in dont_positions if dont < match_start_position][-1]
    return last_do_before_match_start_position > last_dont_before_match_start_position

matches_2 = re.finditer(mult_pair_regex, raw_input, re.MULTILINE) # reusing the same regex, matches was consumed above

# Part 2
print("Day 3 Part 2:\n", sum([mult_pair(match, do_or_dont(match.start(), do_positions, dont_positions)) for match in matches_2]))