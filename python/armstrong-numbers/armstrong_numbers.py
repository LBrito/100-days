def is_armstrong(number):
    exponent = len(str(number))
    total = 0
    for d in str(number):
        total += int(d) ** exponent
    return total == number
