import re
from claim import Claim


def parse_input(data):
    claims = []
    pattern = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for claim in data:
        match = pattern.match(claim)
        if match:
            claim_id = match.group(1)
            left = int(match.group(2))
            top = int(match.group(3))
            width = int(match.group(4))
            height = int(match.group(5))
            claim = Claim(claim_id, left, top, width, height)
            claims.append(claim)

    return claims


def init_fabric(height, width):
    fabric = []
    for i in range(0, height):
        row = [0] * width
        fabric.append(row)

    return fabric


def get_dimensions(claims):
    max_height = 0
    max_width = 0
    for claim in claims:
        if claim.top + claim.height > max_height:
            max_height = claim.top + claim.height
        if claim.left + claim.width > max_width:
            max_width = claim.left + claim.width

    return max_height, max_width


def plot_claim(fabric, claim):
    for i in range(claim.top, claim.top + claim.height):
        for j in range(claim.left, claim.left + claim.width):
            fabric[i][j] += 1


def find_overlap(fabric):
    total_overlap = 0
    for row in fabric:
        for col in row:
            if col > 1:
                total_overlap += 1
    return total_overlap


def run(input):
    claims = parse_input(input)
    height, width = get_dimensions(claims)
    fabric = init_fabric(height, width)
    for claim in claims:
        plot_claim(fabric, claim)
    print(find_overlap(fabric))


# Test
# input = [
#     '#1 @ 1,3: 4x4',
#     '#2 @ 3,1: 4x4',
#     '#3 @ 5,5: 2x2'
# ]
# run(input)

with open('input.txt', 'r') as data:
    run(data)
