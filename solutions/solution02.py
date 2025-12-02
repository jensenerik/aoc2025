from math import log10

from . import read_input

EXAMPLE = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

BIGGEST = 6812585188

input = read_input("02")


def parse_input(input: str) -> list[tuple[int, ...]]:
    ranges = []
    single_line_input = "".join(input.splitlines())
    for range in single_line_input.split(","):
        ranges.append(tuple([int(end) for end in range.split("-")]))
    return ranges


def run_repeats(max_val: int = BIGGEST, twice: bool = True) -> set[int]:
    repeats = set()
    for note in range(1, 10 ** (int(log10(max_val) / 2) + 1)):
        max_copies = 2 if twice else int((log10(max_val) + 1) / (int(log10(note)) + 1))
        for copy_cnt in range(2, max_copies + 1):
            repeat = int(str(note) * copy_cnt)
            if repeat <= max_val:
                repeats.add(repeat)
    return repeats


def check_for_repeats(ranges: list[tuple[int, ...]], repeats: set[int]) -> int:
    captured = []
    for repeat in repeats:
        for range in ranges:
            if repeat >= range[0] and repeat <= range[1]:
                captured.append(repeat)
    return sum(captured)


assert check_for_repeats(parse_input(EXAMPLE), run_repeats()) == 1227775554
assert check_for_repeats(parse_input(EXAMPLE), run_repeats(twice=False)) == 4174379265
print(check_for_repeats(parse_input(input), run_repeats()))
print(check_for_repeats(parse_input(input), run_repeats(twice=False)))
