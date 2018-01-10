

def circular_add(start, amount, rng=(30, 126)):
    output = start + amount
    if output > rng[1]:
        output -= rng[1]
        output += rng[0] - 1
        if output > rng[1]:
            output = circular_add(rng[1], output - rng[1], rng=rng)

    return output


def circular_subtract(start, amount, rng=(30, 126)):
    output = start - amount

    if output < rng[0]:
        output += rng[1] + 1
        output -= rng[0]
        if output < rng[0]:
            output = circular_subtract(rng[0], rng[0] - output, rng=rng)

    return output


def dial_add(start, amount, rng=(30, 126)):
    o = start + amount
    if o > rng[1]:
        return o % rng[1] + (rng[0] - 1)

    return o


def dial_sub(start, amount, rng=(30, 126)):
    output = start - amount

    # Handle negative numbers.
    if output < 0:
        subtract_amount = abs(output) + 32
        output = (rng[1] - subtract_amount) + 1
        if output < rng[0]:
            output = dial_sub(rng[0], rng[0] - output, rng=rng)

    # Handle outputs less than the lower end of the range.
    if output < rng[0]:
        output = rng[1] - (rng[0] % (start - amount)) + 1

    return output


