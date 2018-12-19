import re
from day3.claim import Claim


def parse_input():
    claims = []
    pattern = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for claim in open('input.txt', 'r'):
        match = pattern.match(claim)
        if match:
            claim_id = match.group(1)
            left = match.group(2)
            top = match.group(3)
            width = match.group(4)
            height = match.group(5)
            claim = Claim(claim_id, left, top, width, height)

    claims.append(claim)


def plot_claims(height, width):
    rows = []
    for i in range(0, height):
        row = [None] * width
        rows.append(row)


def get_dimensions(claims):
    max_height = 0
    max_width = 0
    for claim in claims:
        if claim.height > max_height:
            max_height = claim.height
        if claim.width > max_width:
            max_width = claim.width

    return max_height, max_width

