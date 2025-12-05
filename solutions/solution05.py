from . import read_input

EXAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def parse_input(input_block: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ingreds = []
    changed_type = False
    for row in input_block.splitlines():
        if len(row) == 0:
            changed_type = True
        elif changed_type:
            ingreds.append(int(row))
        else:
            split_range = row.split("-")
            ranges.append((int(split_range[0]), int(split_range[1])))
    return ranges, ingreds


def check_overlap(base: int, fresh_range: tuple[int, int]) -> bool:
    if (base >= fresh_range[0]) and (base <= fresh_range[1]):
        return True
    return False


def check_ranges(ranges: list[tuple[int, int]], ingreds: list[int]) -> int:
    fresh_count = 0
    for ingr in ingreds:
        for fresh_range in ranges:
            if check_overlap(ingr, fresh_range):
                fresh_count += 1
                break
    return fresh_count


def consolidate_ranges(ranges: list[tuple[int, int]]) -> int:
    consol_ranges: set[tuple[int, int]] = set()
    for new_range in ranges:
        first_overlap: tuple[int, int] | None = None
        second_overlap: tuple[int, int] | None = None
        interior_ranges: set[tuple[int, int]] = set()
        for consol_range in consol_ranges:
            if check_overlap(new_range[0], consol_range):
                first_overlap = consol_range
            if check_overlap(new_range[1], consol_range):
                second_overlap = consol_range
            if check_overlap(consol_range[0], new_range) and check_overlap(consol_range[1], new_range):
                if (consol_range != first_overlap) and (consol_range != second_overlap):
                    interior_ranges.add(consol_range)
        consol_ranges.difference_update(interior_ranges)
        if (first_overlap is None) and (second_overlap is None):
            consol_ranges.add(new_range)
        elif first_overlap is None:
            assert second_overlap is not None
            consol_ranges.remove(second_overlap)
            consol_ranges.add((new_range[0], second_overlap[1]))
        elif second_overlap is None:
            assert first_overlap is not None
            consol_ranges.remove(first_overlap)
            consol_ranges.add((first_overlap[0], new_range[1]))
        else:
            assert (first_overlap is not None) and (second_overlap is not None)
            consol_ranges.remove(first_overlap)
            if first_overlap != second_overlap:
                consol_ranges.remove(second_overlap)
            consol_ranges.add((first_overlap[0], second_overlap[1]))
    return total_range_length(consol_ranges)


def total_range_length(ranges: set[tuple[int, int]]) -> int:
    return sum([(fr[1] - fr[0] + 1) for fr in ranges])


assert check_ranges(*parse_input(EXAMPLE)) == 3
print(check_ranges(*parse_input(read_input("05"))))
assert consolidate_ranges(parse_input(EXAMPLE)[0]) == 14
print(consolidate_ranges(parse_input(read_input("05"))[0]))
