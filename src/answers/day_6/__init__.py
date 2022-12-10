from utils import read_day_input_file

DAY = 6

def get_chars(input_str, buffer_size):
    current = input_str[:buffer_size-1]
    for i, c in enumerate(input_str):
        if i < buffer_size-1:
            continue
        if i == buffer_size-1:
            current += c
        else:
            current = current[1:] + c
        if len(set(current)) == buffer_size:
            return i+1


def solve(input_str):
    buffer_size = 4
    return get_chars(input_str, buffer_size)

def solve_part_two(input_str):
    buffer_size = 14
    return get_chars(input_str, buffer_size)


if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))
