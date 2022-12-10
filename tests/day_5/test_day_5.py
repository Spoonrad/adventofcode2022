from answers.day_5 import solve, parse_stacks, parse_orders, solve_part_two
from tests.utils import read_day_input_file

def test_day_5():
    input_str = read_day_input_file(5)
    assert solve(input_str) == 'CMZ'

def test_parse_stacks():
    input_str = read_day_input_file(5)
    stacks_str = input_str.split('\n\n')[0]
    assert parse_stacks(stacks_str) == {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }

def test_parse_orders():
    input_str = read_day_input_file(5)
    orders_str = input_str.split('\n\n')[1]
    assert parse_orders(orders_str)[0] == (1, 2, 1)

def test_solve():
    input_str = read_day_input_file(5)
    assert solve(input_str) == 'CMZ'

def test_solve_part_two():
    input_str = read_day_input_file(5)
    assert solve_part_two(input_str) == 'MCD'


