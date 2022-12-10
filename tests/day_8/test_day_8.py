from answers.day_8 import solve, parse_grid, scan_tree
from tests.utils import read_day_input_file

DAY = 8

def test_day_8():
    input_str = read_day_input_file(DAY)
    nb_visible, _ = solve(input_str)
    assert nb_visible == 21

def test_scenic_score():
    input_str = read_day_input_file(DAY)
    grid = parse_grid(input_str)
    tree_properties = scan_tree(grid, 2, 1)
    assert tree_properties.scenic_score == 4

def test_parse_grid():
    input_str = "123\n456\n789"

    grid = parse_grid(input_str)
    assert grid == {
        0: {
            0: 1,
            1: 4,
            2: 7
        },
        1: {
            0: 2,
            1: 5,
            2: 8
        },
        2: {
            0: 3,
            1: 6,
            2: 9
        }
    }
    assert grid[1][2] == 8

