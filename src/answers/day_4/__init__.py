from utils import read_day_input_file

DAY = 4

def parse_pairs(input_str) -> list[list[tuple[int, int]]]:
    lines = input_str.split('\n')
    pairs = [[]]
    for line in lines:
        if len(pairs[-1]) == 2:
            pairs.append([])
        for group in line.split(','):
            min, max = (int(val_str) for val_str in group.split('-'))
            pairs[-1].append((min, max))

    return pairs

def solve(input_str):
    pairs = parse_pairs(input_str)
    nb_fully_contained = 0
    for pair in pairs:
        min_a, max_a = pair[0]
        min_b, max_b = pair[1]
        if (((min_a - min_b) <= 0 and (max_a - max_b) >= 0) or
            ((min_a - min_b) >= 0 and (max_a - max_b) <= 0)):
            nb_fully_contained += 1
    return nb_fully_contained

def solve_part_two(input_str):
    pairs = parse_pairs(input_str)
    nb_intersections = 0
    for pair in pairs:
        min_a, max_a = pair[0]
        min_b, max_b = pair[1]
        if min_a <= max_b and min_b <= max_a:
            nb_intersections += 1

    return nb_intersections

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))

