from answers.day_6 import solve, solve_part_two
from tests.utils import read_day_input_file

def test_day_6():
    input_str = read_day_input_file(6)
    assert solve(input_str) == 7

def test_day_6_part_two():
    input_str = read_day_input_file(6)
    assert solve_part_two(input_str) == 19
