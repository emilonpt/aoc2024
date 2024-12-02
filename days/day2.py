
raw_input = open("./inputs/day2.txt", "r").read()

raw_input_lines = raw_input.split("\n")

reports = [[int(x) for x in line.split(" ")] for line in raw_input_lines]

def check_is_safe(report: list, smoothable = False) -> bool:
    if (report == sorted(report)) or (report == sorted(report, reverse=True)):
        diffs = [abs(x) for x in [report[i+1] - report[i] for i in range(len(report)-1)]]
        if min(diffs) >= 1 and max(diffs) <= 3:
            return True
        
    if smoothable:
        return check_if_unsafe_report_is_smoothable(report)
    
    return False

def check_if_unsafe_report_is_smoothable(unsafe_report: list) -> bool:
    for i in range(len(unsafe_report)):
        if check_is_safe(unsafe_report[:i] + unsafe_report[i+1:]):
            return True
    return False

# Part 1
print("Day 2 Part 1:\n", sum([check_is_safe(report) for report in reports]))

# Part 2
print("Day 2 Part 2:\n", sum([check_is_safe(report, smoothable=True) for report in reports]))