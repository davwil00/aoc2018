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


def total_distance_from_all_coordinates(x, y, coordinates):
    return sum([calculate_distance((x, y), (coordinate.x, coordinate.y)) for coordinate in coordinates])


def populate_distances(coordinates, coordinates_grid):
    distances_grid = init_grid(coordinates)
    for y in range(0, len(distances_grid)):
        for x in range(0, len(distances_grid[y])):
            distances_grid[y][x] = total_distance_from_all_coordinates(x, y, coordinates)

    return distances_grid


def read_coordinates(input):
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    coordinates = []
    for coordinate in input:
        components = coordinate.split(', ')
        coordinates.append(Coordinate(int(components[0]), int(components[1])))
    return coordinates


def find_safe_region_size(distances_grid, threshold):
    size = 0
    for row in distances_grid:
        for col in row:
            if col < threshold:
                size += 1
    return size


def run():
    with open('input.txt', 'r') as input:
        coordinates = read_coordinates(input)
        grid = init_grid(coordinates)
        plot_coordinates(coordinates, grid)
        distances_grid = populate_distances(coordinates, grid)
        print(find_safe_region_size(distances_grid, 10000))


run()
