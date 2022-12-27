from answers.day_15 import solve, parse, get_sensor_coverage
from tests.utils import read_day_input_file

DAY = 15

def test_parse():

  input_str = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16"""

  assert parse(input_str) == {
    (2, 18): (-2, 15),
    (9, 16): (10, 16)
  }

def test_sensor_coverage():
  sensor = (3, 2)
  beacon = (2, 1)

  assert get_sensor_coverage(sensor, beacon) == {
    (3, 0),
    (2, 1),
    (3, 1),
    (4, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (5, 2),
    (2, 3),
    (3, 3),
    (4, 3),
    (3, 4),
  }

def test_day_15():
  assert solve(read_day_input_file(DAY), 10) == 26
