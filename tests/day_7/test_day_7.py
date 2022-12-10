from answers.day_7 import parse_tree, calc_dir_size, solve, solve_part_two
from tests.utils import read_day_input_file


def test_calc_dir_size():
    tree = {
        'a': {
            'b': {
                'x': 100
            },
            'y': 400
        }
    }
    assert calc_dir_size({}, tree, [])[0] == {
        '': 500,
        'a': 500,
        'a/b': 100,
    }


def test_parse_tree():
    input_str = read_day_input_file(7)
    assert parse_tree(input_str) == {
        'a': {
            'e': {
                'i': 584
            },
            'f': 29116,
            'g': 2557,
            'h.lst': 62596
        },
        'b.txt': 14848514,
        'c.dat': 8504156,
        'd': {
            'j': 4060174,
            'd.log': 8033020,
            'd.ext': 5626152,
            'k': 7214296
        }
    }

def test_solve():
    assert solve(read_day_input_file(7)) == 95437

def test_solve_part_two():
    assert solve_part_two(read_day_input_file(7)) == 24933642
