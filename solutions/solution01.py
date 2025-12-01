from . import read_input

EXAMPLE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

EXTRA_EXAMPLE = "L774"

input = read_input("01")

START_VAL = 50
MODULUS = 100


def parse_moves(moves: str) -> list[int]:
    return [(-1) ** (move[0] == "L") * int(move[1:]) for move in moves.splitlines()]


def detect_zeros(moves: list[int], start_val: int, modulus: int) -> tuple[int, int]:
    zero_count = 0
    en_passant_count = 0
    curr_val = start_val
    for move in moves:
        raw_new_val = curr_val + move
        en_passant_count += int(raw_new_val <= 0 and curr_val != 0) + abs(raw_new_val) // modulus
        curr_val = raw_new_val % modulus
        zero_count += int(curr_val == 0)
    return zero_count, en_passant_count


assert detect_zeros(parse_moves(EXAMPLE), START_VAL, MODULUS) == (3, 6)
assert detect_zeros(parse_moves(EXTRA_EXAMPLE), START_VAL, MODULUS) == (0, 8)

print(detect_zeros(parse_moves(read_input("01")), START_VAL, MODULUS))
