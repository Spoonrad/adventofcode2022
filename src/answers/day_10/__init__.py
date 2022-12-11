from utils import read_day_input_file, chunks
from abc import ABC, abstractmethod
import re

DAY = 10

class CRT():

    ROW_SIZE = 40

    def __init__(self, cpu):
        self._current_position = 0
        self._cpu = cpu
        self._current_row_pixels = ""

    @property
    def sprite_middle_position(self):
        return self._cpu.get_register('X')

    def draw(self):
        self._current_row_pixels += ('#' if abs(self._current_position - self.sprite_middle_position) <= 1 else '.')
        if len(self._current_row_pixels) == CRT.ROW_SIZE:
            print(self._current_row_pixels)
            self._current_row_pixels = ""
            self._current_position = 0
        else:
            self._current_position += 1

class CPU():

    RECORD_AT_CYCLES = [
        20, 60, 100, 140, 180, 220
    ]

    def __init__(self):
        self.init_registers()
        self._cycles = 0
        self._tracked_signal_strengths = {}
        self._current_instruction = None
        self._current_instruction_cycles_left = 0
        self.crt = CRT(self)

    def init_registers(self):
        self._registers = {
            'X': 1
        }

    def get_register(self, name):
        return self._registers[name]

    def add_to_register(self, name, k):
        self._registers[name] += k

    @property
    def cycles(self):
        return self._cycles

    @property
    def signal_strength(self):
        return self._cycles * self._registers['X']

    @property
    def tracked_signal_strengths(self):
        return self._tracked_signal_strengths

    @cycles.setter
    def cycles(self, new_cycles):
        self._cycles = new_cycles
        if self._cycles in CPU.RECORD_AT_CYCLES:
            self._tracked_signal_strengths[self._cycles] = self.signal_strength

    def run(self, instruction_queue):
        for instruction_cls, instruction_args in instruction_queue:
            self.begin_instruction(instruction_cls(self, *instruction_args))
            while self._current_instruction:
                self.new_cycle()

    def new_cycle(self):
        self.cycles = self._cycles + 1

        self.crt.draw()

        self._current_instruction_cycles_left -= 1
        if self._current_instruction_cycles_left == 0:
            self.finish_current_instruction()

    def begin_instruction(self, instruction):
        self._current_instruction = instruction
        self._current_instruction_cycles_left = self._current_instruction.CYCLES

    def finish_current_instruction(self):
        if self._current_instruction:
            self._current_instruction.run()
        self._current_instruction = None

class Instruction(ABC):

    CYCLES: int

    def __init__(self, cpu, *args, **kwargs):
        self._cpu = cpu

    @abstractmethod
    def run(self):
        raise NotImplementedError()

def instruction_queue(input_str):
    for line in input_str.split('\n'):
        yield parse_instruction(line)

def parse_instruction(line):
    pattern_matchers = [
        (u"noop", Noop, ()),
        (u"add([a-z]) (-?[0-9]+)", AddToRegister, (lambda char: char.upper(), int))
    ]
    for pattern, instruction, arg_mappers in pattern_matchers:
        match = re.match(pattern, line)
        if not match:
            continue
        return instruction, [mapper(raw_match) for raw_match, mapper in zip(match.groups(), arg_mappers)]

    raise Exception(f'instruction not found: {line}')

class Noop(Instruction):

    CYCLES = 1

    def run(self):
        return

class AddToRegister(Instruction):

    CYCLES = 2

    def __init__(self, cpu, register, increment):
        super().__init__(cpu)
        self._register = register
        self._increment = increment

    def run(self):
        self._cpu.add_to_register(self._register, self._increment)

def solve(input_str):
    cpu = CPU()
    cpu.run(instruction_queue(input_str))
    total_tracked_signal_strength = sum(cpu.tracked_signal_strengths.values())
    return total_tracked_signal_strength

if __name__ == '__main__':
    print(solve(read_day_input_file(DAY)))
