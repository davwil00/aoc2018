from collections import namedtuple, defaultdict
import sys
import string


def calculate_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def init_grid(coordinates):
    width = 0
    height = 0
    for coordinate in coordinates:
        if coordinate.x > width:
            width = coordinate.x
        if coordinate.y > height:
            height = coordinate.y

    grid = []
    for i in range(0, height + 1):
        grid.append([None] * (width + 1))

    return grid


def plot_coordinates(coordinates, grid):
    for i, coordinate in enumerate(coordinates):
        grid[coordinate.y][coordinate.x] = i


def find_nearest_neighbour(x, y, coordinates):
    nearest = None
    min_distance = sys.maxsize
    for i, coodinate in enumerate(coordinates):
        distance = calculate_distance((x, y), (coodinate.x, coodinate.y))
        if distance < min_distance:
            min_distance = distance
            nearest = i
        elif distance == min_distance:
            nearest = '.'
    return nearest


def populate_distances(coordinates, grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] is None:
                grid[y][x] = find_nearest_neighbour(x, y, coordinates)


def read_coordinates(input):
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    coordinates = []
    for coordinate in input:
        components = coordinate.split(', ')
        coordinates.append(Coordinate(int(components[0]), int(components[1])))
    return coordinates


def find_infinite_zones(grid):
    infinite_zones = set()
    [infinite_zones.add(zone) for zone in grid[0]]
    [infinite_zones.add(zone) for zone in grid[-1]]
    [infinite_zones.add(row[0]) for row in grid]
    return infinite_zones


def find_largest_finite_area(grid):
    counts = defaultdict(int)
    for row in grid:
        for col in row:
            if col != '.':
                counts[col] += 1

    infinite_zones = find_infinite_zones(grid)
    for c in infinite_zones:
        if c in counts:
            del(counts[c])
    largest_area = max(counts, key=lambda key: counts.get(key))
    return largest_area, counts[largest_area]


def run():
    with open('input.txt', 'r') as input:
        coordinates = read_coordinates(input)
        grid = init_grid(coordinates)
        plot_coordinates(coordinates, grid)
        populate_distances(coordinates, grid)
        # [print(row) for row in grid]
        print(find_largest_finite_area(grid))


run()
