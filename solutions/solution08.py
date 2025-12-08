from math import prod
from typing import Any

from solutions import read_input

EXAMPLE = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def parse_input(input_block: str) -> list[tuple[int, int, int]]:
    return [
        (int(row.split(",")[0]), int(row.split(",")[1]), int(row.split(",")[2])) for row in input_block.splitlines()
    ]


def full_distance(coords: list[tuple[int, int, int]]) -> list[tuple[int, int, Any]]:
    distances: list[tuple[int, int, Any]] = []
    for i, c1 in enumerate(coords):
        for j, c2 in enumerate(coords[i + 1 :]):
            distances.append((i, j + i + 1, sum([(c1[j] - c2[j]) ** 2 for j in range(3)]) ** 0.5))
    return sorted(distances, key=(lambda x: x[2]))


def calc_groups(input_block: str, iterations: int) -> dict[int, int]:
    coords = parse_input(input_block)
    distances = full_distance(coords)
    coord_pointers = list(range(len(coords)))
    for iter in range(iterations):
        i, j, _ = distances[iter]
        i_val = coord_pointers[i]
        j_val = coord_pointers[j]
        coord_pointers = [i_val if val == j_val else val for val in coord_pointers]
    return {val: coord_pointers.count(val) for val in coord_pointers}


def mult_groups(group_counts: dict[int, int]) -> int:
    return prod(sorted(group_counts.values(), reverse=True)[:3])


def connect_all(input_block: str) -> int:
    coords = parse_input(input_block)
    distances = full_distance(coords)
    coord_pointers = list(range(len(coords)))
    one_group = coord_pointers.count(0) == len(coord_pointers)
    iter = 0
    while not one_group:
        i, j, _ = distances[iter]
        i_val = coord_pointers[i]
        j_val = coord_pointers[j]
        coord_pointers = [i_val if val == j_val else val for val in coord_pointers]
        one_group = coord_pointers.count(coord_pointers[0]) == len(coord_pointers)
        iter += 1
    return coords[i][0] * coords[j][0]


assert mult_groups(calc_groups(EXAMPLE, 10)) == 40
print(mult_groups(calc_groups(read_input("08"), 1000)))

assert connect_all(EXAMPLE) == 25272
print(connect_all(read_input("08")))
