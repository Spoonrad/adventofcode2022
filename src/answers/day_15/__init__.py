from utils import read_day_input_file
import re

DAY = 15

def parse(input_str):

  _map = {}

  for line in input_str.split('\n'):
    sensor_x, sensor_y, beacon_x, beacon_y = re.search(u'x=(-?[0-9]+), y=(-?[0-9]+).+x=(-?[0-9]+), y=(-?[0-9]+)', line).groups()
    _map[(int(sensor_x), int(sensor_y))] = (int(beacon_x), int(beacon_y))

  return _map

def dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_sensor_coverage(sensor, beacon):
  coverage = set()
  sensor_x, sensor_y = sensor
  sensor_beacon_dist = dist(sensor, beacon)
  moves = list(range(sensor_beacon_dist +1))
  moves += [m*-1 for m in moves]
  for delta_x in moves:
    for delta_y in moves:
      check_x = sensor_x + delta_x
      check_y = sensor_y + delta_y
      _dist = dist(sensor, (check_x, check_y))
      if _dist <= sensor_beacon_dist:
        coverage.add((check_x, check_y))
  return coverage

def coverage_at_y(y, _map):
  coverage = set()
  for sensor, beacon in _map.items():
    coverage = coverage.union(get_sensor_coverage(sensor, beacon))
  return [coords for coords in coverage if coords[1] == y and coords not in _map.values()]

def solve(input_str):
  _map = parse(input_str)

  cov_intervals = []

  for y in range(20):
    for sensor, beacon in _map.items():
      _dist = dist(sensor, beacon)
      delta_y = abs(sensor[1] - y)
      nb_cov = _dist - delta_y
      if nb_cov > 0:
        cov_interval = (sensor[0] - nb_cov, sensor[0] + nb_cov)
        cov_intervals.append(cov_interval)
    uncov = [(0, 20)]
    for _uncov in uncov:
      for cov_interval in cov_intervals:
        


  nb_tiles_covered = 0

  for x in range(4000000):
    cov_ = []
    for cov_min, cov_max in cov_intervals:
      if x >= cov_min and x <= cov_max:
        nb_tiles_covered += 1
        cov_.append()
        break

  return nb_tiles_covered

if __name__ == '__main__':
  print(solve(read_day_input_file(DAY), 2000000))
