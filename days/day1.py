raw_input = open("./inputs/day1.txt", "r").read()

raw_input_lines = raw_input.split("\n")

left_column = [int(x) for x in [line.split("   ")[0] for line in raw_input_lines]]
left_column.sort()

right_column = [int(x) for x in [line.split("   ")[1] for line in raw_input_lines]]
right_column.sort()

# Part 1
print("Day 1 Part 1:\n", sum(abs(x-y) for x, y in zip(left_column, right_column)))

unique_left = set(left_column)

def compute_similarity_score(i,rc):
    return i*rc.count(i)

# Part 2
print("Day 1 Part 2:\n", sum(compute_similarity_score(i,right_column) for i in unique_left))