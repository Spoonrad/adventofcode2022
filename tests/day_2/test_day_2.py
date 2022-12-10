from answers.day_2 import solve, solve_part_two
from tests.utils import read_day_input_file

def test_day_2():
    input_str = read_day_input_file(day=2)
    assert solve(input_str) == 15

def test_day_2_part_2():
    input_str = read_day_input_file(day=2)
    assert solve_part_two(input_str) == 12