

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


class Dial(object):
    def __init__(self, start, rng=(30, 126)):
        self.start = start
        self.rng = rng
        self.full_rng = rng[1] - rng[0]
        self.rng_list = list(range(rng[0], rng[1] + 1))
        self.pointer = self.rng_list.index(start)
        self.current = self.rng_list[self.pointer]

    def _increment(self):
        if self.pointer == len(self.rng_list) - 1:
            self.pointer = 0
            self.current = self.rng_list[self.pointer]
            return True
        self.pointer += 1
        self.current = self.rng_list[self.pointer]
        return True

    def _decrement(self):
        if self.pointer == 0:
            self.pointer = len(self.rng_list) - 1
            self.current = self.rng_list[self.pointer]
            return True

        self.pointer -= 1
        self.current = self.rng_list[self.pointer]
        return True

    def set_pointer(self, point):
        self.pointer = self.rng_list.index(point)
        self.current = self.rng_list[self.pointer]
        return self

    def add(self, amount):
        while amount > self.rng[1]:
            amount = amount // self.full_rng + amount % self.full_rng

        for i in range(amount):
            self._increment()

        return self.current

    def sub(self, amount):
        # Reduce the amount of iterations we need to perform.
        while amount > self.rng[1]:
            amount = amount // self.full_rng + amount % self.full_rng

        for i in range(amount):
            self._decrement()

        return self.current


# d = Dial(90)
# print(d.add(17334))
# print(d.add(5))
# print(d.sub(17334))
# print()
# print(circular_add(90, 17334, rng=(30, 126)))
# print(circular_subtract(90, 17334, rng=(30, 126)))



