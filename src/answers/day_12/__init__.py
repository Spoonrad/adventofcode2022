from utils import read_day_input_file
from collections import defaultdict
from enum import Enum
from math import inf

DAY = 12

class OutOfBounds(Exception):
    pass

class Cell():

    def __init__(self, height, x, y, is_start=False, is_end=False):
        self.x = x
        self.y = y
        self.height = height
        self.is_start = is_start
        self.is_end = is_end

    def __str__(self):
        if self.is_start:
            return 'S'
        if self.is_end:
            return 'E'
        return str(self.height)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.height == other.height and
                self.x == other.x and
                self.y == other.y)

    @staticmethod
    def parse_cell(_input, x, y):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        heights = {**{k: i for i, k in enumerate(alphabet)},
                   'S': 0,
                   'E': len(alphabet) - 1
                   }
        return Cell(
            x=x,
            y=y,
            height=heights[_input],
            is_start=(_input == 'S'),
            is_end=(_input == 'E'))


def parse_grid(input_str):
    grid = defaultdict(dict)
    start_cell = None
    end_cell = None

    for y, line in enumerate(input_str.split('\n')):
        for x, _input in enumerate(line):
            cell = Cell.parse_cell(_input, x, y)
            if cell.is_start:
                start_cell = cell
            if cell.is_end:
                end_cell = cell
            grid[x][y] = cell

    return grid, start_cell, end_cell

class MoveDirection(Enum):
    LEFT = "left"
    RIGHT = "right"
    DOWN = "down"
    UP = "up"

def get_adjacent_cell(grid, current, direction):
    mapper = {
        MoveDirection.LEFT: (current.x - 1, current.y),
        MoveDirection.RIGHT: (current.x + 1, current.y),
        MoveDirection.DOWN: (current.x, current.y - 1),
        MoveDirection.UP: (current.x, current.y + 1)
    }
    x, y = mapper[direction]
    try:
        return grid[x][y]
    except KeyError:
        raise OutOfBounds(f"{x}{y}")

def shortest_path_predecessors(grid, start_cell):

    width = len(grid.keys())
    height = len(grid[0].keys())
    unvisited = set([(x, y) for x in range(width) for y in range(height)])
    shortest_distances = {(start_cell.x, start_cell.y): 0}

    # best predecessor of given position
    pred = {}

    while unvisited:

        # get unvisited cell with known shortest distance
        current_shortest = None
        for (x, y), d in shortest_distances.items():
            if (x, y) in unvisited and (current_shortest is None or d < current_shortest[-1]):
                current_shortest = (x, y, d)

        if current_shortest is None:
            raise Exception('No shortest path exists')

        current_cell = grid[current_shortest[0]][current_shortest[1]]
        current_dist = current_shortest[-1]

        # check all adjacent cells
        for direction in MoveDirection:
            try:
                adjacent_cell = get_adjacent_cell(grid, current_cell, direction)
                if (current_cell.height - adjacent_cell.height) >= -1 and (current_dist + 1) < shortest_distances.get((adjacent_cell.x, adjacent_cell.y), inf):
                    shortest_distances[(adjacent_cell.x, adjacent_cell.y)] = current_dist + 1
                    pred[(adjacent_cell.x, adjacent_cell.y)] = (current_cell.x, current_cell.y)

            except OutOfBounds:
                continue

        unvisited.remove((current_cell.x, current_cell.y))

    return pred

def solve(input_str):

    grid, start_cell, end_cell = parse_grid(input_str)

    draw = defaultdict(dict)
    for y, line in enumerate(input_str.split('\n')):
        for x, h in enumerate(line):
            draw[x][y] = h

    pred = shortest_path_predecessors(grid, start_cell)
    current_x, current_y = end_cell.x, end_cell.y
    nb_steps = 0

    while (current_x, current_y) != (start_cell.x, start_cell.y):
        current_x, current_y = pred[current_x, current_y]
        draw[current_x][current_y] = 'X'
        nb_steps += 1

    width = len(draw.keys())
    height = len(draw[0].keys())

    print('\n\n')
    for y in range(height):
        line = ""
        for x in range(width):
            line += draw[x][y]
        print(line)

    return nb_steps

def solve_part_two(input_str):

    grid, start_cell, end_cell = parse_grid(input_str)

    starting_positions = []

    current_min = None

    draw = defaultdict(dict)
    for y, line in enumerate(input_str.split('\n')):
        for x, h in enumerate(line):
            draw[x][y] = h
            if h in ('a', 'S'):
                starting_positions.append((x, y))

    for starting_position in starting_positions:

        draw = defaultdict(dict)
        for y, line in enumerate(input_str.split('\n')):
            for x, h in enumerate(line):
                draw[x][y] = h

        skip = False
        try:
            pred = shortest_path_predecessors(grid, start_cell)
        except Exception:
            continue

        current_x, current_y = end_cell.x, end_cell.y
        nb_steps = 0
        start_cell = grid[starting_position[0]][starting_position[1]]

        while (current_x, current_y) != (start_cell.x, start_cell.y):
            current_x, current_y = pred.get((current_x, current_y), (None, None))
            if not current_x:
                skip = True
                break
            if skip:
                continue
            draw[current_x][current_y] = 'X'
            nb_steps += 1

        width = len(draw.keys())
        height = len(draw[0].keys())

        print('\n')
        for y in range(height):
            line = ""
            for x in range(width):
                line += draw[x][y]
            print(line)

        current_min = nb_steps if not current_min else min(current_min, nb_steps)

    return current_min+1

if __name__ == '__main__':
    # print(solve(read_day_input_file(DAY)))
    print(solve_part_two(read_day_input_file(DAY)))