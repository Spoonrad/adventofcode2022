from utils import read_day_input_file
import re
from functools import cmp_to_key

DAY = 13


def parse_list(substring):
    values = []

    int_value = ""

    char_index = 0
    while char_index < len(substring):
        char = substring[char_index]
        if re.match('[0-9]', char):
            int_value += char
        elif int_value:
            values.append(int(int_value))
            int_value = ""
        if char == '[' and char_index > 0:
            # When parsing a nested list, skip the scanned characters
            nested_values, nb_chars = parse_list(substring[char_index:])
            values.append(nested_values)
            char_index += nb_chars
        elif char == ']':
            return values, char_index
        char_index += 1
    return values, None

def parse_pairs(input_str):
    pairs = []
    current_pair = []
    for line in input_str.split('\n'):
        if line == '':
            continue
        current_pair.append(parse_list(line)[0])
        if len(current_pair) == 2:
            pairs.append(tuple(current_pair))
            current_pair = []
    return pairs

def compare(left, right):
    print(f"compare {left} with {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        for item_index, left_item in enumerate(left):
            if item_index < len(right):
                is_same_order = compare(left_item, right[item_index])
                if is_same_order != None:
                    return is_same_order
            else:
                return 1
        if len(right) > len(left):
            return -1
    elif isinstance(left, list):
        return compare(left, [right])
    elif isinstance(right, list):
        return compare([left], right)

def solve(input_str):
    total_indexes_right_order = 0
    for index, pair in enumerate(parse_pairs(input_str)):
        pair_number = index + 1
        print(f'---- PAIR {pair_number} ----')
        print(pair[0])
        print(pair[1])
        is_right_order = compare(pair[0], pair[1])
        if is_right_order:
            total_indexes_right_order += pair_number
        print(f'---- RESULT: {"RIGHT ORDER" if is_right_order else "WRONG ORDER"} -----')
        print('-----------------------------')
    return total_indexes_right_order

def solve_part_two(input_str):
    print('--------PART TWO-----------')
    packets = [parse_list(line)[0] for line in input_str.split('\n') if line != '']

    divider_prod = 1
    divider_packets = [[[2]], [[6]]]

    print('\n\n----- SORTED PACKETS -----')

    for index, sorted_packet in enumerate(sorted(packets + divider_packets, key=cmp_to_key(compare))):
        print(sorted_packet)
        if sorted_packet in divider_packets:
            divider_prod *= (index+1)
    return divider_prod


if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print('\n\n')
    print(solve_part_two(input_str))