from answers.day_13 import solve, parse_list, parse_pairs, compare, solve_part_two
from tests.utils import read_day_input_file

DAY = 13

def test_day_13():
    input_str = read_day_input_file(DAY)
    assert solve(input_str) == 13

def test_day_13_part_2():
    input_str = read_day_input_file(DAY)
    assert solve_part_two(input_str) == 140

def test_parse_list():
    assert parse_list("[0,10]")[0] == [0,10]
    assert parse_list("[0,[0,1]]")[0] == [0, [0, 1]]
    assert parse_list("[0,[1,[0,1],2], [1,0]]")[0] == [0, [1, [0, 1], 2], [1, 0]]

def test_parse_pairs():
    input_str = """[0,1]
[1,0]

[2,3]
[3,2]"""
    assert parse_pairs(input_str) == [
        ([0,1], [1,0]),
        ([2,3], [3,2])
    ]

def test_compare():
    assert compare([9], [[8,7,6]]) == 1
    assert compare([[4,4],4,4], [[4,4],4,4,4]) == -1