from typing import Any
from utils import read_day_input_file

DAY = 1

def _calories_by_elf(input_str: str) -> list[int]:
    lines = input_str.split('\n')
    calories_by_elf = [0]
    for line in lines:
        if line != '':
            calories_by_elf[-1] += int(line)
        else:
            calories_by_elf.append(0)
    return calories_by_elf

def solve(input_str: str) -> Any:
    return max(_calories_by_elf(input_str))

def solve_part_two(input_str: str) -> Any:
    calories_by_elf = _calories_by_elf(input_str)
    return sum(sorted(calories_by_elf, reverse=True)[:3])

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))

