from collections import namedtuple

GRID_SERIAL_NUMBER = 8444
MAX_SQUARE_SIZE = 300

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


# Function to preprcess input mat[M][N].
# This function mainly fills aux[M][N]
# such that aux[i][j] stores sum
# of elements from (0,0) to (i,j)
# from https://www.geeksforgeeks.org/submatrix-sum-queries/
def pre_process(mat, aux):
    grid_size = len(mat)
    # Copy first row of mat[][] to aux[][]
    for i in range(0, grid_size, 1):
        aux[0][i] = mat[0][i]

        # Do column wise sum
    for i in range(1, grid_size, 1):
        for j in range(0, grid_size, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

            # Do row wise sum
    for i in range(0, grid_size, 1):
        for j in range(1, grid_size, 1):
            aux[i][j] += aux[i][j - 1]


# between (tli, tlj) and (rbi, rbj) using aux[][]
# which is built by the preprocess function
# adapted from https://www.geeksforgeeks.org/submatrix-sum-queries/
def sum_query(aux, top_left: Coordinate, bottom_right: Coordinate):
    # result is now sum of elements
    # between (0, 0) and (rbi, rbj)
    res = aux[bottom_right.y - 1][bottom_right.x - 1]

    # Remove elements between (0, 0)
    # and (tli-1, rbj)
    if top_left.y > 1:
        res = res - aux[top_left.y - 2][bottom_right.x - 1]

    # Remove elements between (0, 0)
    # and (rbi, tlj-1)
    if top_left.x > 1:
        res = res - aux[bottom_right.y - 1][top_left.x - 2]

    # Add aux[tli-1][tlj-1] as elements
    # between (0, 0) and (tli-1, tlj-1)
    # are subtracted twice
    if top_left.y > 1 and top_left.x > 1:
        res = res + aux[top_left.y - 2][top_left.x - 2]

    return res


def run():
    max_power = 0
    max_power_coords = Coordinate(0, 0)
    max_square_size = 0
    grid = create_square(Coordinate(1,1), MAX_SQUARE_SIZE)
    summed_area_table = [[0 for i in range(300)]
       for j in range(300)]
    pre_process(grid, summed_area_table)
    for square_size in range(1, 300):
        for x in range(1, MAX_SQUARE_SIZE - square_size + 1):
            for y in range(1, MAX_SQUARE_SIZE - square_size + 1):
                top_left = Coordinate(x, y)
                bottom_right = Coordinate(x + square_size - 1, y + square_size - 1)
                total_power = sum_query(summed_area_table, top_left, bottom_right)
                if total_power > max_power:
                    max_power = total_power
                    max_power_coords = top_left
                    max_square_size = square_size

    print(f'Top left coordinate: {max_power_coords}')
    print(f'Max power: {max_power}')
    print(f'Square size: {max_square_size}')

run()