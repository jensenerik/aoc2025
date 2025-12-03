from . import read_input

EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


def find_top_pair(nums: str) -> int:
    top_pair = (0, 0)
    for ten_pos, ten_dig in enumerate(nums):
        ten_int = int(ten_dig)
        if ten_int > top_pair[0] and ten_pos + 1 < len(nums):
            top_pair = (ten_int, 0)
            for one_dig in nums[ten_pos + 1 :]:
                one_int = int(one_dig)
                if one_int > top_pair[1]:
                    top_pair = (ten_int, one_int)
    return top_pair[0] * 10 + top_pair[1]


def sum_pairs(block: str) -> int:
    return sum([find_top_pair(row) for row in block.splitlines()])


def find_top_group(nums: str, positions: int) -> int:
    current = ""
    leftover = nums
    positions_to_fill = positions
    while positions_to_fill > 0:
        top_num = max(leftover[: 1 - positions_to_fill]) if positions_to_fill > 1 else max(leftover)
        top_pos = leftover.find(top_num)
        current = current + top_num
        leftover = leftover[top_pos + 1 :]
        positions_to_fill = positions_to_fill - 1
    return int(current)


def sum_block(block: str, positions: int) -> int:
    return sum([find_top_group(row, positions) for row in block.splitlines()])


assert sum_pairs(EXAMPLE) == 357
assert sum_block(EXAMPLE, 2) == 357
assert sum_block(EXAMPLE, 12) == 3121910778619
print(sum_pairs(read_input("03")))
print(sum_block(read_input("03"), 2))
print(sum_block(read_input("03"), 12))
