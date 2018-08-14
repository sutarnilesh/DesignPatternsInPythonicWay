import abc


class OddNumbers(object):
    """An Iterable object"""

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return OddIterator(self)


class OddIterator(object):
    """An iterator"""

    def __init__(self, container):
        self.container = container
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.counter > self.container.maximum:
            raise StopIteration
        return self.counter


if __name__ == "__main__":
    numbers = OddNumbers(7)
    for n in numbers:
       print(n)
    print("**************************")
    it = iter(OddNumbers(7))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))