from collections import defaultdict, deque
from itertools import cycle


def run_simulation(marbles, players):
    marbles = list(range(1, marbles + 1))
    players = list(range(1, players + 1))
    player_iter = cycle(players)
    circle = deque()
    circle.append(0)
    scores = defaultdict(int)

    for marble in marbles:
        player = next(player_iter)
        if marble > 0 and marble % 23 == 0:
            scores[player] += marble
            # remove the marble 7 counter-clockwise and add to score
            circle.rotate(-7)
            scores[player] += circle.popleft()
            circle.rotate(1)
        else:
            circle.rotate(1)
            circle.appendleft(marble)

    return max(scores.values())


assert(run_simulation(25, 9) == 32)
assert(run_simulation(1618, 10) == 8317)
assert(run_simulation(7999, 13) == 146373)
assert(run_simulation(1104, 17) == 2764)
assert(run_simulation(6111, 21) == 54718)
assert(run_simulation(5807, 30) == 37305)

print(run_simulation(71082, 413))
print(run_simulation(7108200, 413))
