import math


def score(x, y):
    distance = math.sqrt(((0-x)**2) + ((0-y)**2))
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0

