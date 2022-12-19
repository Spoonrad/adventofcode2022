from answers.day_12 import solve, parse_grid, Cell, solve_part_two
from tests.utils import read_day_input_file

DAY = 12

def test_day_12():
    assert solve(read_day_input_file(DAY)) == 31

def test_solve_part_two():
    assert solve_part_two(read_day_input_file(DAY)) == 29

def test_parse_grid():
    input_str = """Sbc
def
ghE"""
    assert parse_grid(input_str) == {
        0: {
            0: Cell(0, True),
            1: Cell(3),
            2: Cell(6)
        },
        1: {
            0: Cell(1),
            1: Cell(4),
            2: Cell(7)
        },
        2: {
            0: Cell(2),
            1: Cell(5),
            2: Cell(25, False, True)
        }
    }
