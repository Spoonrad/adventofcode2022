from answers.day_10 import solve
from tests.utils import read_day_input_file

DAY = 10

def test_day_10():
    input_str = read_day_input_file(DAY)
    assert solve(input_str) == 13140