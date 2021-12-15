from aoc import aoc
import numpy as np

FILLED_SPACE = "#"
EMPTY_SPACE = " "


class Instruction:
    def __init__(self, instruction):
        self._axis, self._value = instruction.split('=')

    @property
    def axis(self) -> str:
        return self._axis

    @axis.setter
    def axis(self, value: str) -> None:
        self._axis = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


def parse_input(input: list[str]):
    points = set()
    instructions = []
    for line in input:
        if line.startswith('fold along'):
            axis, index = line.split()[2].split('=')
            instructions.append((axis, int(index)))
        elif line != '':
            points.add(tuple(map(int, line.split(','))))
    return points, instructions


def create_grid_from_input(input_data):
    max_col = max([p[0] for p in input_data])
    max_row = max([p[1] for p in input_data])
    grid = [[FILLED_SPACE if (col, row) in input_data else EMPTY_SPACE for col in range(max_col + 1)] for row in range(max_row + 1)]
    return grid


def fold_points(points, folding_axis, folding_index):
    if folding_axis == "x":
        def fold_point(column, row):
            return folding_index - abs(folding_index - column), row
    else:  # fold_axis == "y"
        def fold_point(column, row):
            return column, folding_index - abs(folding_index - row)

    return {fold_point(*point) for point in points}


def print_points(points: set[tuple[int, int]]):
    max_column = max(point[0] for point in points)
    max_row = max(point[1] for point in points)
    for row in range(max_row + 1):
        for column in range(max_column + 1):
            print(FILLED_SPACE if (column, row) in points else EMPTY_SPACE, end="")

        print("\n", end="")



input = aoc.read_input('../input/in.txt')
coords, folds = parse_input(input)

for axis, index in folds:
    coords = fold_points(coords, axis, index)

print_points(coords)