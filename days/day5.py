raw_input = open("./inputs/day5.txt", "r").read()

raw_input_rules = raw_input.split("\n\n")[0].split("\n")
raw_input_updates = raw_input.split("\n\n")[1].split("\n")
raw_input_updates = [update.split(",") for update in raw_input_updates]

rules_dict = {}

for rule in raw_input_rules:
    rule_left, rule_right = rule.split("|")
    for rule in [rule_left, rule_right]:
        if rule not in rules_dict:
            rules_dict[rule] = {}
            rules_dict[rule]["must_be_before"] = []
            rules_dict[rule]["must_be_after"] = []
    rules_dict[rule_left]["must_be_before"].extend([rule_right])
    rules_dict[rule_right]["must_be_after"].extend([rule_left])

def check_valid_update_order(rules_dict, update_order):
    for i in range(len(update_order)):
        for j in range(i+1, len(update_order)):
            if update_order[j] in rules_dict[update_order[i]]["must_be_after"]:
                return False
        for j in range(i-1, -1, -1):
            if update_order[j] in rules_dict[update_order[i]]["must_be_before"]:
                return False
    return True

valid_updates = []
invalid_updates = []
for update in raw_input_updates:
    if check_valid_update_order(rules_dict, update):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

print("Day 5 Part 1: ", sum([int(vu[len(vu)//2]) for vu in valid_updates]))

# Part 2

# recursively fix the invalid update order
def fix_invalid_update_order(rules_dict, update_order):
    for i in range(len(update_order)):
        for j in range(i+1, len(update_order)):
            if update_order[j] in rules_dict[update_order[i]]["must_be_after"]:
                update_order.insert(i, update_order.pop(j))
                return fix_invalid_update_order(rules_dict, update_order)
        for j in range(i-1, -1, -1):
            if update_order[j] in rules_dict[update_order[i]]["must_be_before"]:
                update_order.insert(j, update_order.pop(i))
                return fix_invalid_update_order(rules_dict, update_order)
    return update_order

fixed_invalid_updates = [fix_invalid_update_order(rules_dict, update) for update in invalid_updates]

print("Day 5 Part 2: ", sum([int(fiu[len(fiu)//2]) for fiu in fixed_invalid_updates]))