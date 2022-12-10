from enum import Enum
from utils import read_day_input_file
from collections import defaultdict
from dataclasses import dataclass

DAY = 8

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    DOWN = "down"
    UP = "up"

def move(x, y, direction):
    return {
        Direction.LEFT: _move_left,
        Direction.RIGHT: _move_right,
        Direction.DOWN: _move_down,
        Direction.UP: _move_up
    }[direction](x, y)

def _move_left(x, y):
    return x-1, y

def _move_right(x, y):
    return x+1, y

def _move_up(x, y):
    return x, y+1

def _move_down(x, y):
    return x, y-1

@dataclass
class TreeDirectionProperties:
    direction: Direction
    is_hidden: bool
    viewing_distance: int

@dataclass
class TreeProperties:
    is_visible: bool
    scenic_score: int

def parse_grid(input_str):
    grid = defaultdict(dict)
    for y, line in enumerate(input_str.split('\n')):
        for x, h in enumerate(line):
            grid[x][y] = int(h)
    return grid

def scan_tree(grid, x, y):
    scenic_score = 1
    is_visible = False
    for direction in Direction:
        direction_properties = scan_direction(grid, direction, x, y)
        if not direction_properties.is_hidden:
            is_visible = True
        scenic_score *= direction_properties.viewing_distance
    return TreeProperties(
        is_visible=is_visible,
        scenic_score=scenic_score
    )


def scan_direction(grid, direction, x, y):
    size = len(grid)
    height = grid[x][y]
    viewing_distance = 0
    check_x, check_y = move(x, y, direction)
    while all([coord >= 0 and coord < size for coord in [check_x, check_y]]):
        viewing_distance += 1
        check_height = grid[check_x][check_y]
        if check_height >= height:
            return TreeDirectionProperties(direction=direction, is_hidden=True, viewing_distance=viewing_distance)
        check_x, check_y = move(check_x, check_y, direction)
    return TreeDirectionProperties(direction=direction, is_hidden=False, viewing_distance=viewing_distance)

def solve(input_str):
    grid = parse_grid(input_str)
    size = len(grid)
    max_scenic_score = 0
    nb_visible = 0
    for x in range(size):
        for y in range(size):
            tree_properties = scan_tree(grid, x, y)
            max_scenic_score = max(max_scenic_score, tree_properties.scenic_score)
            nb_visible += int(tree_properties.is_visible)

    return nb_visible, max_scenic_score

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
