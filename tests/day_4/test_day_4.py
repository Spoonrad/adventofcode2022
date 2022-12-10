from answers.day_4 import solve, parse_pairs, solve_part_two
from tests.utils import read_day_input_file

DAY = 4

def test_day_4():
    input_str = read_day_input_file(day=DAY)
    assert solve(input_str) == 2

def test_day_4_part_two():
    input_str = read_day_input_file(day=DAY)
    assert solve_part_two(input_str) == 4

def test_parse_pairs():
    input_str = read_day_input_file(day=DAY)
    assert parse_pairs(input_str)[0] == [(2, 4), (6, 8)]

