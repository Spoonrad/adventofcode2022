from answers.day_14 import solve, Grid, Material, solve_part_two
import answers.day_14
from tests.utils import read_day_input_file

DAY = 14
INPUT_STR = read_day_input_file(DAY)

def test_day_14():
    answers.day_14.DEBUG = True
    assert solve(read_day_input_file(DAY)) == 24

def test_day_14_part_2():
    answers.day_14.DEBUG = True
    assert solve_part_two(read_day_input_file(DAY)) == 93
def test_parse_grid():
    rock = Material.ROCK
    grid = Grid.parse_grid(INPUT_STR)
    assert grid.cells == Grid(cells={
        k: rock for k in [
        (498, 4),
        (498, 5),
        (498, 6),
        (497, 6),
        (496, 6),
        (503, 4),
        (502, 4),
        (502, 5),
        (502, 6),
        (502, 7),
        (502, 8),
        (502, 9),
        (501, 9),
        (500, 9),
        (499, 9),
        (498, 9),
        (497, 9),
        (496, 9),
        (495, 9),
        (494, 9)
        ]
    }).cells

    grid.draw()
