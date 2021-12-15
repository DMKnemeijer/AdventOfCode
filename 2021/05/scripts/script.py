from aoc import aoc
from collections import namedtuple
import numpy as np

GRID_SIZE = 1000
DRAW_DIAGONALS = True

input = aoc.read_input('../input/in.txt')
Point = namedtuple('Point', ['x', 'y'])


def generate_grid_lines(raw_input):
    lines = []
    for line in raw_input:
        p1, p2 = line.split(' -> ')
        p1 = Point(*map(int, p1.split(',')))
        p2 = Point(*map(int, p2.split(',')))
        lines.append((p1, p2))
    return lines


def draw_grid_lines(grid_lines, draw_diagonal=False):
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    for p1, p2 in grid_lines:
        if p1.x == p2.x:
            # X coordinates are equal, line is vertical
            (y1, y2) = sorted([p1.y, p2.y])
            grid[p1.x, y1:y2+1] += 1
        elif p1.y == p2.y:
            # Y coordinates are equal, line is horizontal
            (x1, x2) = sorted([p1.x, p2.x])
            grid[x1:x2+1, p1.y] += 1
        elif draw_diagonal:
            # For simplicities sake, only draw lines left to right
            if p1.x > p2.x:
                (p1, p2) = (p2, p1)
            if p1.y < p2.y:
                # Descending diagonal
                for i in range(p2.x + 1 - p1.x):
                    grid[p1.x + i, p1.y + i] += 1
            else:
                # Ascending diagonal
                for i in range(p2.x + 1 - p1.x):
                    grid[p1.x + i, p1.y - i] += 1
    return grid


lines = generate_grid_lines(input)
grid_a = draw_grid_lines(lines)
grid_b = draw_grid_lines(lines, draw_diagonal=True)

print(f"Intersections in grid A: {np.count_nonzero(grid_a > 1)}")
print(f"Intersections in grid B: {np.count_nonzero(grid_b > 1)}")
