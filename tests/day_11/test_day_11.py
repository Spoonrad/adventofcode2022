from tests.utils import read_day_input_file
from answers.day_11 import solve

DAY = 11

def test_day_11():
    assert solve(read_day_input_file(DAY), 20, True) == 10605
    assert solve(read_day_input_file(DAY), 10000, False) == 2713310158
