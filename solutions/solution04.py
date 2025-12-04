from . import read_input, v_add

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def parse_diagram(diagram: str) -> set[tuple[int, int]]:
    rolls = set()
    for row_num, row in enumerate(diagram.splitlines()):
        for col_num, item in enumerate(row):
            if item == "@":
                rolls.add((row_num, col_num))
    return rolls


def neighbor_vectors() -> set[tuple[int, int]]:
    vectors = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not ((i == 0) and (j == 0)):
                vectors.add((i, j))
    return vectors


def calc_neighbors(rolls: set[tuple[int, int]]) -> tuple[int, set[tuple[int, int]]]:
    neighbor_map: dict[tuple[int, int], int] = {}
    neighbor_vects = neighbor_vectors()
    for roll_loc in rolls:
        for vect in neighbor_vects:
            neighbor = v_add(roll_loc, vect)
            neighbor_map[neighbor] = 1 + neighbor_map.get(neighbor, 0)
    high_neighbors = [k for k in neighbor_map.keys() if neighbor_map[k] >= 4]
    return len(rolls.difference(high_neighbors)), rolls.intersection(high_neighbors)


def repeatedly_remove(rolls: set[tuple[int, int]]) -> int:
    total_removed = 0
    current_rolls = rolls
    finished = False
    while not finished:
        new_removed, current_rolls = calc_neighbors(current_rolls)
        total_removed += new_removed
        finished = new_removed == 0
    return total_removed


assert calc_neighbors(parse_diagram(EXAMPLE))[0] == 13
assert repeatedly_remove(parse_diagram(EXAMPLE)) == 43
print(calc_neighbors(parse_diagram(read_input("04")))[0])
print(repeatedly_remove(parse_diagram(read_input("04"))))
