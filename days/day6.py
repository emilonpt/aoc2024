#increase max recursion depth
import sys
import threading
max_recursion_depth = 100000000
sys.setrecursionlimit(max_recursion_depth)

raw_input = open("./inputs/day6.txt", "r").read()

raw_input_lines = raw_input.split("\n")

grid = [[v for v in line] for line in raw_input_lines]

starting_position = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] in ["^",">","v","<"]]

def rotate_right(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"
    
def get_next_pos(pos, direction):
    x, y = pos
    if direction == "^":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "v":
        y += 1
    elif direction == "<":
        x -= 1
    return (x, y)

# Part 1 - follow move algorithm and count the number of visited positions

def move(pos, direction, grid, visited_positions):
    x, y = pos
    visited_positions[(x,y)] = True
    next_pos = get_next_pos(pos, direction)
    if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
        return visited_positions
    if grid[next_pos[1]][next_pos[0]] == "#":
        direction = rotate_right(direction)
    else:
        pos = next_pos
    return move(pos, direction, grid, visited_positions)

visited_positions = move(starting_position[0], grid[starting_position[0][1]][starting_position[0][0]], grid, {})

print("Day 6 Part 1: ", len(visited_positions))

# Part 2 - brute force adding a new # (wall) at each possible new position (except the starting position) and counting the number of
# added walls that result in the guard entering a loop

def add_wall(pos, grid):
    x, y = pos
    new_grid = [row.copy() for row in grid]
    new_grid[y][x] = "#"
    return new_grid

all_grids = [add_wall((x,y), grid) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "."]

num_grids = len(all_grids)

visited_positions = {}

def move2(pos, direction, grid, visited_positions, i):
    if pos in visited_positions.keys():
        if visited_positions[pos] == direction:
            return True
    x, y = pos
    next_pos = get_next_pos(pos, direction)
    if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
        return False
    if grid[next_pos[1]][next_pos[0]] == "#":
        direction = rotate_right(direction)
    else:
        visited_positions[(x,y)] = direction
        pos = next_pos
    return move2(pos, direction, grid, visited_positions, i)

loops_found = 0

for i in range(num_grids):
    visited_positions = {}
    loops_found += move2(starting_position[0], grid[starting_position[0][1]][starting_position[0][0]], all_grids[i], visited_positions, i)

print("Day 6 Part 2: ", loops_found)