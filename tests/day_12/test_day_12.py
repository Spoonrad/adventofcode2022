from answers.day_12 import solve, Grid, Cell, solve_part_two
from tests.utils import read_day_input_file

DAY = 12

def test_parse_grid():
    input_str = (
"""Sbc
def
ghE""")
    start_cell = Cell(0, 0, 0, True, False)
    end_cell =  Cell(25, 2, 2, False, True)
    assert Grid.parse_grid(input_str) == Grid(cells={
        0: {
            0: start_cell,
            1: Cell(3, 0, 1),
            2: Cell(6, 0, 2)
        },
        1: {
            0: Cell(1, 1, 0),
            1: Cell(4, 1, 1),
            2: Cell(7, 1, 2)
        },
        2: {
            0: Cell(2, 2, 0),
            1: Cell(5, 2, 1),
            2: end_cell
        }
    }, start_cell=start_cell, end_cell=end_cell)

def test_day_12():
    assert solve(read_day_input_file(DAY)) == 31

def test_day_12_part_2():
    assert solve_part_two(read_day_input_file(DAY)) == 29