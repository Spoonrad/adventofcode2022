from answers.day_3 import solve, solve_part_two
from tests.utils import read_day_input_file

def test_day_3():
    input_str = read_day_input_file(day=3)
    assert solve(input_str) == 157
    assert solve_part_two(input_str) == 70