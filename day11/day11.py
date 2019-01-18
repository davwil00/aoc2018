from collections import namedtuple
from itertools import chain

GRID_SERIAL_NUMBER = 8444
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


def create_square(top_left):
    grid = []
    for y in range(top_left.y, top_left.y + 3):
        row = []
        for x in range(top_left.x, top_left.x + 3):
            row.append(calculate_power_level(x, y))
        grid.append(row)
    return grid


def calculate_grid_sum(grid):
    return sum(chain.from_iterable(grid))


def run():
    max_power = 0
    max_power_coords = Coordinate(0,0)
    for x in range(1, 298):
        for y in range(1, 298):
            coordinates = Coordinate(x, y)
            grid = create_square(coordinates)
            total_power = calculate_grid_sum(grid)
            if total_power > max_power:
                max_power = total_power
                max_power_coords = coordinates
    print(max_power_coords)
    print(total_power)


grid = create_square(Coordinate(21, 61))
[print(row) for row in grid]
print(calculate_grid_sum(grid))

run()