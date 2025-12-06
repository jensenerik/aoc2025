from math import prod

from . import read_input

EXAMPLE = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """  # noqa: W291


def parse_input(block: str) -> list[list[str]]:
    return [row.split() for row in block.splitlines()]


def transpose_rows(parsed_block: list[list[str]]) -> list[list[str]]:
    output: list[list[str]] = []
    for row in parsed_block:
        for col_num, col in enumerate(row):
            if len(output) <= col_num:
                output.append([])
            output[col_num].append(col)
    return output


def transpose_positions(block: str) -> int:
    parsed = [list(row) for row in block.splitlines()]
    operator = ""
    values: list[int] = []
    total_sum = 0
    for col in reversed(transpose_rows(parsed)):
        if len("".join(col).strip()) == 0:
            values = []
            operator = ""
        else:
            operator = col[-1]
            values.append(int("".join(col[:-1])))
            if operator == "+":
                total_sum += sum(values)
            elif operator == "*":
                total_sum += prod(values)
    return total_sum


def calc_rows(transposed: list[list[str]]) -> int:
    total_sum = 0
    for row in transposed:
        operation = row[-1]
        values = [int(item) for item in row[:-1]]
        total_sum += sum(values) if operation == "+" else prod(values)
    return total_sum


assert calc_rows(transpose_rows(parse_input(EXAMPLE))) == 4277556
print(calc_rows(transpose_rows(parse_input(read_input("06")))))

assert transpose_positions(EXAMPLE) == 3263827
print(transpose_positions(read_input("06")))
