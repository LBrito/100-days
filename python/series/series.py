def slices(series, length):

    if len(series) < length:
        raise ValueError("Slice length is too large!")
    elif length < 1:
        raise ValueError("Slice length is not valid!")
    elif len(series) < 1:
        raise ValueError("Series cannot be empty!")

    return [
        series_item for series_item in
        [series[x:x + length] for x in range(len(series))]
        if len(series_item) == length
    ]
