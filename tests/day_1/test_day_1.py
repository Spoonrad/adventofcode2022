from answers.day_1 import solve, solve_part_two
from tests.utils import read_day_input_file

def test_day_1():
    input_str = read_day_input_file(day=1)
    assert solve(input_str) == 24000

def test_day_1_part_2():
    input_str = read_day_input_file(day=1)
    assert solve_part_two(input_str) == 45000
