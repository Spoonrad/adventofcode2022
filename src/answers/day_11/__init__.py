from utils import read_day_input_file
from typing import Callable, Any
import re
from math import prod

DAY = 11

COMMON_DIVIDOR = 0

class Symbol:

    PATTERN: str
    ARG_MAPPERS = list[Callable[[str], Any]]

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def parse(cls, match):
        return cls(*[arg_mapper(arg_str) for arg_mapper, arg_str in zip(cls.ARG_MAPPERS, match.groups())])

    def eval(self, worry):
        raise NotImplementedError()

class CurrentWorry(Symbol):

    PATTERN = "old"
    ARG_MAPPERS = []

    def eval(self, worry):
        return worry

class Integer(Symbol):

    PATTERN = "([0-9]+)"
    ARG_MAPPERS = [int]

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = value

    def eval(self, worry):
        return self._value

class Operator:

    def __init__(self, name, character, eval, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = character
        self._name = name
        self._eval = eval

    def eval(self, l, r):
        return self._eval(l, r)

OPERATORS = [
    Operator("ADD", "+", lambda l, r: l+r),
    Operator("SUBSTRACT", "-", lambda l, r: l-r),
    Operator("MULTIPLY", "*", lambda l, r: l*r),
    Operator("DIVIDE", "/", lambda l, r: l/r)
]

class Operation:
    def __init__(self, l, r, operator):
        self._l = l
        self._r = r
        self._operator = operator

    def eval(self, worry):
        result = self._operator.eval(self._l.eval(worry), self._r.eval(worry))
        return result

class WorryTest:
    pass

class IsDivisibleBy(WorryTest):

    def __init__(self, number, target_on_success, target_on_failure):
        self.number = number
        self._target_on_success = target_on_success
        self._target_on_failure = target_on_failure

    def eval(self, worry):
        return self._target_on_success if worry % self.number == 0 else self._target_on_failure

def parse_operator(symbol):
    for operator in OPERATORS:
        if operator.symbol == symbol:
            return operator

class Monkey:
    def __init__(self, items, operation, test, manage_worries):
        self._items = items
        self._operation = operation
        self.test = test
        self._manage_worries = manage_worries
        self.nb_inspected_items = 0

    def receive_item(self, item):
        self._items.append(item)

    def _inspect(self, item):
        self.nb_inspected_items += 1
        return self._operation.eval(item)

    def _get_bored(self, item):
        # When we don't divide by 3, we need to keep worry low
        # by doing item mod (product of all monkey test dividors)
        global COMMON_DIVIDOR
        return int(item / 3) if self._manage_worries else item % COMMON_DIVIDOR

    def _throw_item(self, item, target):
        target.receive_item(item)

    def run_turn(self, monkeys):
        while len(self._items) > 0:
            item = self._items.pop(0)
            item = self._inspect(item)
            item = self._get_bored(item)
            target = self.test.eval(item)
            self._throw_item(item, monkeys[target])

def parse_items(line):
    return [int(n) for n in line.split(':')[-1].split(',')]

def parse_symbol(characters):
    for symbol_cls in [CurrentWorry, Integer]:
        match = re.match(symbol_cls.PATTERN, characters)
        if match:
            return symbol_cls.parse(match)

def parse_operation(line):
    symbols = line.split('=')[-1].strip().split(' ')
    return Operation(l=parse_symbol(symbols[0]), r=parse_symbol(symbols[-1]), operator=parse_operator(symbols[1]))

def parse_test(lines):

    end_of_line_int = lambda l: int(l.split(' ')[-1])

    return IsDivisibleBy(
        *[end_of_line_int(line) for line in lines]
    )

def parse_monkeys(input_str, manage_worries):

    monkeys = []

    index = 0
    for block in input_str.split('\n\n'):
        lines = block.split('\n')
        items = parse_items(lines[1])
        operation = parse_operation(lines[2])
        test = parse_test(lines[3:])
        monkeys.append(Monkey(
            items=items,
            operation=operation,
            test=test,
            manage_worries=manage_worries
        ))
        index += 1

    global COMMON_DIVIDOR
    COMMON_DIVIDOR = prod([monkey.test.number for monkey in monkeys])

    return monkeys

def run_round(monkeys):
    for monkey in monkeys:
        monkey.run_turn(monkeys)

def solve(input_str, nb_rounds, manage_worries):

    monkeys = parse_monkeys(input_str, manage_worries)

    round = 0
    while round < nb_rounds:
        round += 1
        run_round(monkeys)

    most_active_monkeys = sorted(monkeys, key=lambda monkey: monkey.nb_inspected_items, reverse=True)
    monkey_business = prod([monkey.nb_inspected_items for monkey in most_active_monkeys[:2]])

    return monkey_business

if __name__ == '__main__':
    print(solve(read_day_input_file(DAY), 20, True))
    print(solve(read_day_input_file(DAY), 10000, False))
