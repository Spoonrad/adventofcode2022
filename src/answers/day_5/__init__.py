from utils import read_day_input_file
from collections import defaultdict
import re
from abc import abstractmethod, ABC

DAY = 5
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def parse_stacks(stack_str):
    stacks = defaultdict(list)
    for line in stack_str.split('\n'):
        for char_index, char in enumerate(line):
            current_index = char_index // 4 + 1
            if char in ALPHABET:
                stacks[current_index].append(char)
    for index, stack in stacks.items():
        stacks[index] = list(reversed(stack))
    return stacks

def parse_orders(orders_str):
    orders = []
    for line in orders_str.split('\n'):
        nb, start, end = map(int, re.fullmatch(u'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups())
        orders.append((nb, start, end))
    return orders


class CrateMover(ABC):

    def __init__(self, stacks):
        self._stacks = stacks

    @abstractmethod
    def move_boxes(self, nb, s, e):
        raise NotImplementedError

class CrateMover9000(CrateMover):

    def _move_box(self, s, e):
        box = self._stacks[s].pop()
        self._stacks[e].append(box)
        return self._stacks

    def move_boxes(self, nb, s, e):
        for _ in range(nb):
            self._stacks = self._move_box(s, e)
        return self._stacks

class CrateMover9001(CrateMover):
    def move_boxes(self, nb, s, e):
        boxes = self._stacks[s][-nb:]
        self._stacks[s] = self._stacks[s][:-nb]
        self._stacks[e] += boxes
        return self._stacks


def parse(input_str):
    stack_str, orders_str = tuple(input_str.split('\n\n'))
    stacks = parse_stacks(stack_str)
    orders = parse_orders(orders_str)
    return dict(sorted(stacks.items())), orders

def solve(input_str):
    stacks, orders = parse(input_str)
    crate_mover = CrateMover9000(stacks=stacks)
    for nb, start, end in orders:
        stacks = crate_mover.move_boxes(nb, start, end)
    return ''.join([stack[-1] for stack in stacks.values()])

def solve_part_two(input_str):
    stacks, orders = parse(input_str)
    crate_mover = CrateMover9001(stacks=stacks)
    for nb, start, end in orders:
        stacks = crate_mover.move_boxes(nb, start, end)
    return ''.join([stack[-1] for stack in stacks.values()])


if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))


