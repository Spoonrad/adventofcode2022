from utils import read_day_input_file
from enum import Enum
from functools import total_ordering

DAY = 2

@total_ordering
class Move(Enum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    def __gt__(self, other):
        return any((
            self == Move.ROCK and other == Move.SCISSORS,
            self == Move.PAPER and other == Move.ROCK,
            self == Move.SCISSORS and other == Move.PAPER,
        ))

CHARACTER_MOVE_MAPPER = {
    'A': Move.ROCK,
    'X': Move.ROCK,
    'B': Move.PAPER,
    'Y': Move.PAPER,
    'C': Move.SCISSORS,
    'Z': Move.SCISSORS
}

MOVE_SCORES = {
    Move.ROCK: 1,
    Move.PAPER: 2,
    Move.SCISSORS: 3
}

class RoundOutcome(Enum):
    # from perspective of player (me)
    VICTORY = "VICTORY"
    DRAW = "DRAW"
    DEFEAT = "DEFEAT"

ROUND_OUTCOME_SCORES = {
    RoundOutcome.VICTORY: 6,
    RoundOutcome.DRAW: 3,
    RoundOutcome.DEFEAT: 0
}

def _parse_move(character: str) -> Move:
    return Move(CHARACTER_MOVE_MAPPER[character])

def _parse_round(line):
    round = [_parse_move(char) for char in line.split(' ')]
    return tuple(round)

def _compute_score(opp_move, my_move) -> int:
    outcome = _get_round_outcome(opp_move, my_move)
    score_from_move = MOVE_SCORES[my_move]
    score_from_outcome = ROUND_OUTCOME_SCORES[outcome]
    return score_from_move + score_from_outcome

def _get_round_outcome(opp_move: Move, my_move: Move) -> RoundOutcome:
    if my_move > opp_move:
        return RoundOutcome.VICTORY
    elif my_move == opp_move:
        return RoundOutcome.DRAW
    return RoundOutcome.DEFEAT

def solve(input_str: str):
    total_score = 0
    for line in input_str.split('\n'):
        opp_move, my_move = _parse_round(line)
        score = _compute_score(opp_move, my_move)
        total_score += score
    return total_score

###### PART TWO

CHARACTER_OUTCOME_MAPPER = {
    'X': RoundOutcome.DEFEAT,
    'Y': RoundOutcome.DRAW,
    'Z': RoundOutcome.VICTORY
}

def _get_move_for_outcome(opp_move, outcome):
    if outcome == RoundOutcome.VICTORY:
        for move in Move:
            if move > opp_move:
                return move
    if outcome == RoundOutcome.DEFEAT:
        for move in Move:
            if move < opp_move:
                return move
    return opp_move

def solve_part_two(input_str: str):
    total_score = 0
    for line in input_str.split('\n'):
        opp_move = CHARACTER_MOVE_MAPPER[line[0]]
        outcome = CHARACTER_OUTCOME_MAPPER[line[-1]]
        my_move = _get_move_for_outcome(opp_move, outcome)
        score = _compute_score(opp_move, my_move)
        total_score += score
    return total_score

if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))