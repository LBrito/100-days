from collections import Counter
# Score categories
# Change the values as you see fit
YACHT = (lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0)
ONES = (lambda dice: add_each(dice, 1))
TWOS = (lambda dice: add_each(dice, 2))
THREES = (lambda dice: add_each(dice, 3))
FOURS = (lambda dice: add_each(dice, 4))
FIVES = (lambda dice: add_each(dice, 5))
SIXES = (lambda dice: add_each(dice, 6))
FULL_HOUSE = (lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = (lambda dice: sum(set(map(lambda number: number if dice.count(number) >= 4 else 0, dice))) * 4)
LITTLE_STRAIGHT = (lambda dice: 30 if list(range(1, 6)) == sorted(dice) else 0)
BIG_STRAIGHT = (lambda dice: 30 if list(range(2, 7)) == sorted(dice) else 0)
CHOICE = sum


def add_each(dice, number): return dice.count(number) * number


def score(dice, category):
    return category(dice)
