from collections import defaultdict
from itertools import cycle

NO_OF_MARBLES = 71083
NO_OF_PLAYERS = 413

marbles = list(range(1, NO_OF_MARBLES))
players = list(range(1, NO_OF_PLAYERS + 1))
player_iter = cycle(players)
circle = [0]
scores = defaultdict(int)
index = 0
for marble in marbles:
    player = next(player_iter)
    if marble > 0 and marble % 23 == 0:
        scores[player] += marble
        # remove the marble 7 counter-clockwise and add to score
        index -= 7
        while index < 0:
            index += len(circle)
        scores[player] += circle.pop(index)
    else:
        index += 2
        while index > len(circle):
            index -= len(circle)
        circle.insert(index, marble)


max_score = scores[max(scores, key=lambda key: scores.get(key))]
print(scores)
print(max_score)

if NO_OF_MARBLES == 7:
    assert circle == [0, 4, 2, 5, 1, 6, 3]
    assert scores == {}
elif NO_OF_MARBLES == 25:
    assert circle == [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    assert scores == {5: 32}
elif NO_OF_PLAYERS == 10 and NO_OF_MARBLES == 1619:
    assert max_score == 8317
