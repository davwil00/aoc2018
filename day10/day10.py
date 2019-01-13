import re
from collections import defaultdict

regex = re.compile('position=<([ \-\d]+), ([ \-\d]+)> velocity=<([ \-\d]+), ([ \-\d]+)>')


class Point:
    def __init__(self, line) -> None:
        pos_x, pos_y, vel_x, vel_y = self.parse(line)
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.vel_x = int(vel_x)
        self.vel_y = int(vel_y)

    def parse(self, line):
        m = regex.match(line)
        if m:
            return m.group(1), m.group(2), m.group(3), m.group(4)
        else:
            raise Exception(f'Unable to parse line {line}')

    def tick(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def __repr__(self) -> str:
        return f'pos: ({self.pos_x}, {self.pos_y}) vel:({self.vel_x}, {self.vel_y})'


def print_points(points, point_map, i):
    rows = sorted(point_map)
    min_x_idx = min(points, key=lambda p: p.pos_x).pos_x
    max_x_idx = max(points, key=lambda p: p.pos_x).pos_x
    if rows[-1] - rows[0] <= 10:
        with open('out.txt', 'a') as out:
            for row_num in range(rows[0], rows[-1] + 1):
                row = point_map[row_num]
                for j in range(min_x_idx, max_x_idx + 1):
                    out.write('#') if j in row else out.write('.')
                out.write('\n')
            out.write('\n\n\n')
            print(i)
            return True


def run():
    with open('input.txt', 'r') as file:
        points = []
        for line in file:
            points.append(Point(line))
        point_map = defaultdict(lambda: [])
        found = False
        i = 1
        while not found:
            [point.tick() for point in points]
            point_map.clear()
            [point_map[point.pos_y].append(point.pos_x) for point in points]
            found = print_points(points, point_map, i)
            i += 1


run()
