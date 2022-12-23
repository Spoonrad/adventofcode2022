from utils import read_day_input_file
from collections import defaultdict
from math import inf

DAY = 12
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class OutOfBounds(Exception):
    pass

class Cell():
    def __init__(self, height, x, y, is_start=False, is_end=False):
        self.height = height
        self.is_start = is_start
        self.is_end = is_end
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.height == other.height and
                self.is_start == other.is_start and
                self.is_end == other.is_end and
                self.x == other.x and
                self.y == other.y)

    def __str__(self):
        if self.is_start:
            return "S"
        elif self.is_end:
            return "E"
        return ALPHABET[self.height]

    @staticmethod
    def parse_cell(input_str, x, y):
        heights = {**{k: i for i, k in enumerate(ALPHABET)},
                   'S': 0,
                   'E': len(ALPHABET) - 1
                   }
        return Cell(
            height=heights[input_str],
            is_start=(input_str == 'S'),
            is_end=(input_str == 'E'),
            x=x,
            y=y)


class Grid():
    def __init__(self, cells, start_cell, end_cell):
        self.cells = cells
        self.width = len(cells.keys())
        self.height = len(cells[0])
        self.start_cell = start_cell
        self.end_cell = end_cell

    def __eq__(self, other):
        if self.width != other.width:
            return False
        if self.height != other.height:
            return False
        for x in range(self.width):
            for y in range(self.height):
                if self.get_cell(x, y) != other.get_cell(x, y):
                    return False
        return True

    @staticmethod
    def parse_grid(input_str):
        cells = defaultdict(dict)
        start_cell = None
        end_cell = None

        for y, line in enumerate(input_str.split('\n')):
            for x, _input in enumerate(line):
                cell = Cell.parse_cell(_input, x, y)
                if cell.is_start:
                    start_cell = cell
                if cell.is_end:
                    end_cell = cell
                cells[x][y] = cell

        return Grid(cells=cells, start_cell=start_cell, end_cell=end_cell)

    def get_cell(self, x, y):
        try:
            return self.cells[x][y]
        except KeyError as exc:
            raise OutOfBounds from exc

    def get_adjacent_cells(self, cell):
        adjacent_cells = []
        for delta_x, delta_y in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]:
            try:
                adj = self.get_cell(cell.x + delta_x, cell.y + delta_y)
                adjacent_cells.append(adj)
            except OutOfBounds:
                pass
        return adjacent_cells

    def draw(self):
        for x in self.cells.keys():
            line = ""
            for cell in self.cells[x]:
                line += str(cell)
            print(line)

def shortest_distance(grid, start_cell=None):

    if not start_cell:
        start_cell = grid.start_cell

    visited = set()
    end_cell = grid.end_cell
    distances = {(start_cell.x, start_cell.y): 0}

    queue = [start_cell]

    while queue:
        current_cell = queue.pop(0)
        for adjacent_cell in grid.get_adjacent_cells(current_cell):
            if (adjacent_cell.x, adjacent_cell.y) not in visited and adjacent_cell.height <= (current_cell.height + 1):
                queue.append(adjacent_cell)
                visited.add((adjacent_cell.x, adjacent_cell.y))
                distance = distances[(current_cell.x, current_cell.y)] + 1
                distances[(adjacent_cell.x, adjacent_cell.y)] = distance
                if adjacent_cell == end_cell:
                    return distance

    return inf
def solve(input_str):
    grid = Grid.parse_grid(input_str)
    _shortest_distance = shortest_distance(grid)
    return _shortest_distance

def solve_part_two(input_str):
    grid = Grid.parse_grid(input_str)

    min_shortest_distance = inf

    for x in range(grid.width):
        for y in range(grid.height):
            cell = grid.get_cell(x, y)
            if cell.height == 0:
                min_shortest_distance = min(shortest_distance(grid, cell), min_shortest_distance)

    return min_shortest_distance

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))
