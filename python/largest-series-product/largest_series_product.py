from functools import reduce


def largest_product(series, size):
    largest = 0
    span = [0] * size

    if len(series) < size or size < 0:
        raise ValueError('Not a valid size')
    if series is None:
        raise ValueError('Invalid series')
    if len(span) < 1:
        return 1

    for number in series:
        span.append(int(number))
        span.pop(0)
        largest = max(largest, reduce(lambda total, value: total * value, span))
    return largest
