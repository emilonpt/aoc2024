raw_input = open("./inputs/day4.txt", "r").read()

raw_input_lines = raw_input.split("\n")

cols = len(raw_input_lines[0])
rows = len(raw_input_lines)

grid = [[v for v in line] for line in raw_input_lines]

All_X_positions = [(x,y) for y in range(rows) for x in range(cols) if grid[y][x] == "X"]

All_M_positions = [(x,y) for y in range(rows) for x in range(cols) if grid[y][x] == "M"]

def find_neighbor_letters(x, y, grid, letter):
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]
    matched_neighbors = []
    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < cols and neighbor[1] >= 0 and neighbor[1] < rows:
            if grid[neighbor[1]][neighbor[0]] == letter:
                matched_neighbors.append(neighbor)
    return matched_neighbors

found_matches = []
for x, y in All_X_positions:
    M_positions = find_neighbor_letters(x, y, grid, "M")
    if len(M_positions) > 0:
        for M_x, M_y in M_positions:
            A_positions = find_neighbor_letters(M_x, M_y, grid, "A")
            A_positions = [A_pos for A_pos in A_positions if A_pos in [(x-2, y), (x+2, y), (x, y-2), (x, y+2), (x-2, y-2), (x+2, y+2), (x-2, y+2), (x+2, y-2)]]
            if len(A_positions) > 0:
                for A_x, A_y in A_positions:
                    S_positions = find_neighbor_letters(A_x, A_y, grid, "S")
                    S_positions = [S_pos for S_pos in S_positions if S_pos in [(x-3, y), (x+3, y), (x, y-3), (x, y+3), (x-3, y-3), (x+3, y+3), (x-3, y+3), (x+3, y-3)]]
                    S_positions = [S_pos for S_pos in S_positions if S_pos in [(M_x-2, M_y), (M_x+2, M_y), (M_x, M_y-2), (M_x, M_y+2), (M_x-2, M_y-2), (M_x+2, M_y+2), (M_x-2, M_y+2), (M_x+2, M_y-2)]]
                    if len(S_positions) > 0:
                        found_matches.append([(x,y), (M_x, M_y), (A_x, A_y), (S_positions[0])])

# Part 1
print("Day 4 Part 1: ", len(found_matches))

def find_diag_letters(x, y, grid, letter):
    neighbors = [(x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]
    matched_neighbors = []
    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < cols and neighbor[1] >= 0 and neighbor[1] < rows:
            if grid[neighbor[1]][neighbor[0]] == letter:
                matched_neighbors.append(neighbor)
    return matched_neighbors

found_matches_2 = []

for M_x, M_y in All_M_positions:
    A_positions = find_diag_letters(M_x, M_y, grid, "A")
    if len(A_positions) > 0:
        for A_x, A_y in A_positions:
            S_positions = find_diag_letters(A_x, A_y, grid, "S")
            S_positions = [S_pos for S_pos in S_positions if S_pos in [(M_x-2, M_y-2), (M_x+2, M_y+2), (M_x-2, M_y+2), (M_x+2, M_y-2)]]
            if len(S_positions) > 0:
                found_matches_2.append([(M_x,M_y),(A_x, A_y), (S_positions[0])])

num_a = {}
for match in found_matches_2:
    if match[1] not in num_a:
        num_a[match[1]] = 1
    else:
        num_a[match[1]] += 1

found_matches_2 = [match for match in found_matches_2 if num_a[match[1]] > 1]

# Part 2
print("Day 4 Part 2: ", len(found_matches_2)//2)