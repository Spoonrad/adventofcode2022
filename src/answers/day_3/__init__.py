from utils import read_day_input_file, chunks
from collections import defaultdict

DAY = 3

PRIORITIES = {char: i + 1 for i, char in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def _find_common_letter(compartments: list[str]):
    compartment_counts = [defaultdict(int) for _ in compartments]
    for i, compartment in enumerate(compartments):
        for char in compartment:
            compartment_counts[i][char] += 1
    compartment_characters = [set(counts.keys()) for counts in compartment_counts]
    intersect = set(compartment_characters[0])
    for _compartment_characters in compartment_characters:
        intersect = intersect.intersection(_compartment_characters)
    return intersect.pop()

def solve(input_str):
    rucksacks = input_str.split('\n')

    total_priority = 0

    for rucksack in rucksacks:
        compartment_size = int(len(rucksack)/2)
        compartments = [rucksack[:compartment_size], rucksack[compartment_size:]]
        common_letter = _find_common_letter(compartments)
        priority = PRIORITIES[common_letter]
        total_priority += priority

    return total_priority

def solve_part_two(input_str):
    rucksacks = input_str.split('\n')
    group_size = 3
    total_priority = 0
    for group in chunks(rucksacks, group_size):
        common_letter = _find_common_letter(group)
        priority = PRIORITIES[common_letter]
        total_priority += priority
    return total_priority


if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))
