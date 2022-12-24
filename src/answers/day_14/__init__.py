from enum import Enum
from utils import read_day_input_file

DAY = 14
DEBUG = False

class Material(Enum):
    ROCK = "#"
    SAND = "o"
    AIR = "."

class Grid:
    def __init__(self, cells, with_floor=False):
        self.cells = cells
        self.floor = None
        if with_floor:
            self.floor = max([coords[1] for coords in self.cells.keys()]) + 2

    def get_cell(self, coords):
        if self.floor and coords[1] == self.floor:
            return Material.ROCK
        return self.cells.get(coords, Material.AIR)

    def set_cell(self, coords, cell):
        self.cells[coords] = cell

    @staticmethod
    def parse_grid(input_str, with_floor=False):
        rocks = {}
        for line in input_str.split('\n'):
            points = line.split(' -> ')
            current_coords = None
            for point in points:
                point_coords = tuple([int(dim) for dim in point.split(',')])
                while current_coords != point_coords:
                    if not current_coords:
                        current_coords = point_coords

                    next_coords = []
                    for current_dim, point_dim in zip(current_coords, point_coords):
                        incr = 0
                        if current_dim < point_dim:
                            incr = 1
                        elif current_dim > point_dim:
                            incr = -1
                        next_coords.append(current_dim + incr)
                    current_coords = tuple(next_coords)

                    rocks[current_coords] = Material.ROCK

        return Grid(rocks, with_floor=with_floor)

    def draw(self):
        print('\n---GRID START---')
        all_x = [coords[0] for coords in self.cells.keys()]
        min_x = min(all_x)
        max_x = max(all_x)

        all_y = [coords[1] for coords in self.cells.keys()]
        min_y = min(all_y)
        max_y = max(all_y)

        for y in range(min_y, max_y+1):
            row = ""
            for x in range(min_x, max_x+1):
                row += self.get_cell((x, y)).value
            print(row)

        print('---GRID END---')

def _get_next_sand_position(grid, current):

    for check in (
            (current[0], current[1] + 1),
            (current[0] - 1, current[1] + 1),
            (current[0] + 1, current[1] + 1)
    ):
        if grid.get_cell(check) == Material.AIR:
            return check

    return current


def sandfall(grid):

    origin = (500, 0)

    max_y = grid.floor if grid.floor else max(coords[1] for coords in grid.cells)

    nb_sand_units = 0

    while True:
        current = origin

        while True:
            _next = _get_next_sand_position(grid, current)
            if _next[1] > max_y:
                return nb_sand_units
            if _next == origin:
                return nb_sand_units + 1

            if _next == current:
                grid.set_cell(_next, Material.SAND)

                if DEBUG:
                    print(grid.draw())

                nb_sand_units += 1
                break

            current = _next

def solve(input_str):
    grid = Grid.parse_grid(input_str)
    nb_sand_units = sandfall(grid)
    return nb_sand_units

def solve_part_two(input_str):
    grid = Grid.parse_grid(input_str, with_floor=True)
    nb_sand_units = sandfall(grid)
    return nb_sand_units

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))