from dataclasses import dataclass
from utils import read_day_input_file
from enum import Enum
from math import sqrt
from copy import copy

DAY = 9

class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

def move(x, y, direction):
    return {
        Direction.LEFT: _move_left,
        Direction.RIGHT: _move_right,
        Direction.DOWN: _move_down,
        Direction.UP: _move_up
    }[direction](x, y)

def _move_left(x, y):
    return x-1, y

def _move_right(x, y):
    return x+1, y

def _move_up(x, y):
    return x, y+1

def _move_down(x, y):
    return x, y-1

@dataclass
class Position:
    x: int
    y: int

@dataclass
class Knot:
    position: Position

    def move(self, direction):
        self.position.x, self.position.y = move(self.position.x, self.position.y, direction)

    def follow(self, knot):

        for get_dim, get_diag_dim, directions, diag_directions in zip(
                [(lambda _knot: _knot.position.x), (lambda _knot: _knot.position.y)],
                [(lambda _knot: _knot.position.y), (lambda _knot: _knot.position.x)],
                [[Direction.RIGHT, Direction.LEFT], [Direction.UP, Direction.DOWN]],
                [[Direction.UP, Direction.DOWN], [Direction.RIGHT, Direction.LEFT]]

        ):
            for sign, direction in zip((1, -1), directions):
                if (get_dim(knot) - get_dim(self))*sign > 1:
                    self.move(direction)
                    for _sign, diag_direction in zip((1, -1), diag_directions):
                        if (get_diag_dim(knot) - get_diag_dim(self))*_sign > 0:
                            self.move(diag_direction)

def solve(input_str, nb_knots):

    visited_positions = set()
    initial_position = Position(0, 0)
    visited_positions.add((initial_position.x, initial_position.y))

    knots = [Knot(copy(initial_position)) for _ in range(nb_knots)]
    head = knots[0]
    tail = knots[-1]

    movements = parse_movements(input_str)
    for direction, nb_moves in movements:
        for _ in range(nb_moves):
            head.move(direction)
            for i in range(nb_knots):
                if i+1 < (nb_knots):
                    leading_knot = knots[i]
                    trailing_knot = knots[i+1]
                    trailing_knot.follow(leading_knot)
            visited_positions.add((tail.position.x, tail.position.y))
    return len(visited_positions)

def parse_movements(input_str):

    move_mapper = {
        'R': Direction.RIGHT,
        'L': Direction.LEFT,
        'D': Direction.DOWN,
        'U': Direction.UP
    }

    movements = []
    for line in input_str.split('\n'):
        move_str, nb_moves_str = line.split(' ')
        move = move_mapper[move_str]
        nb_moves = int(nb_moves_str)
        movements.append((move, nb_moves))
    return movements



if __name__ == '__main__':
    print(solve(read_day_input_file(DAY), 2))
    print(solve(read_day_input_file(DAY), 10))

