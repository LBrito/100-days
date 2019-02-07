def slices(series, length):

    if len(series) < length:
        raise ValueError("Slice length is too large!")
    elif length < 1:
        raise ValueError("Slice length is not valid!")
    elif len(series) < 1:
        raise ValueError("Series cannot be empty!")

    return [series[x:x + length] for x in range(len(series) - length + 1)]
