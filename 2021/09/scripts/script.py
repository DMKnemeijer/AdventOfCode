from aoc import aoc
import numpy as np


def generate_risk_map(height_map: np.array) -> np.array:
    risk_map = np.zeros_like(height_map)
    for y, row in enumerate(height_map):
        for x, value in enumerate(row):
            adjacent_values = aoc.get_adjacent_values(heightmap, x, y)
            if all(adj > height_map[x, y] for adj in adjacent_values):
                risk_map[x, y] = 1 + height_map[x, y]
    return risk_map


def flow(height_map, basins, x, y):
    height = height_map[x, y]
    x_size, y_size = height_map.shape
    if height == 9:
        return
    if x - 1 >= 0 and height - height_map[x - 1, y] > 0:
        return flow(height_map, basins, x-1, y)
    if x + 1 < x_size and height - height_map[x + 1, y] > 0:
        return flow(height_map, basins, x+1, y)
    if y - 1 >= 0 and height - height_map[x, y - 1] > 0:
        return flow(height_map, basins, x, y-1)
    if y + 1 < y_size and height - height_map[x, y + 1] > 0:
        return flow(height_map, basins, x, y+1)
    aoc.logger(f"Adding 1 to basin {x},{y}: {basins[x, y]}")
    basins[x, y] += 1


def generate_basins(height_map):
    basins = np.zeros_like(height_map)
    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            flow(heightmap, basins, i, j)
    return basins


input = aoc.read_input('../input/in.txt')
heightmap = aoc.generate_np(input, nums=True)
riskmap = generate_risk_map(heightmap)
basinmap = generate_basins(heightmap)

print(int(np.sum(riskmap)))
print(np.prod(np.sort(basinmap.flat)[-3:]))
