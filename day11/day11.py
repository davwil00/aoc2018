from collections import namedtuple
from itertools import chain

GRID_SERIAL_NUMBER = 8444
MAX_SQUARE_SIZE = 300
# GRID_SERIAL_NUMBER = 42

Coordinate = namedtuple("Coordinate", ["x", "y"])


def calculate_power_level(x_coord, y_coord):
    rack_id = x_coord + 10
    power_level = rack_id * y_coord
    power_level += GRID_SERIAL_NUMBER
    power_level *= rack_id
    power_level_str = str(power_level)
    power_level = int(power_level_str[-3]) if len(power_level_str) >= 3 else 0
    power_level -= 5
    return power_level


def create_square(top_left, square_size):
    grid = []
    for y in range(top_left.y, top_left.y + square_size):
        row = []
        for x in range(top_left.x, top_left.x + square_size):
            row.append(calculate_power_level(x, y))
        grid.append(row)
    return grid


def calculate_grid_sum(grid):
    return sum(chain.from_iterable(grid))


def run():
    max_power = 0
    max_power_coords = Coordinate(0, 0)
    grid = create_square(Coordinate(1,1), MAX_SQUARE_SIZE)
    for square_size in range(280, MAX_SQUARE_SIZE):
        print(square_size)
        for x in range(1, MAX_SQUARE_SIZE - square_size + 1):
            for y in range(1, MAX_SQUARE_SIZE - square_size + 1):
                max_power, max_power_coords = find_subgrid_power(grid, max_power, max_power_coords, square_size, x, y)
    print(max_power_coords)
    print(max_power)


def find_subgrid_power(grid, max_power, max_power_coords, square_size, x, y):
    coordinates = Coordinate(x, y)
    subgrid = [grid[y + i - 1][x - 1:x + square_size - 1] for i in range(square_size)]
    # subgrid = create_square(Coordinate(x, y), square_size)
    total_power = calculate_grid_sum(subgrid)
    if total_power > max_power:
        max_power = total_power
        max_power_coords = coordinates
    return max_power, max_power_coords


# grid = create_square(Coordinate(21, 61))
# [print(row) for row in grid]
# print(calculate_grid_sum(grid))

run()