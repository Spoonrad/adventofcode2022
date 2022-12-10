from tests.utils import read_day_input_file
from answers.day_9 import solve

DAY = 9

def test_day_9():
    # assert solve(read_day_input_file(DAY), 2) == 88
    assert solve(read_day_input_file(DAY), 10) == 36

