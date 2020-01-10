"""
    Implement & overriding iterator methods
    and generating the fibonacci series
"""
from itertools import islice


class IteratorFibonacci:
    """
        Generating Fibonacci series by overriding
        the __iter__ and __next__ iterators method
    """
    def __init__(self, start=0, end=0):
        self.prev = 0
        self.current = 1
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        # if self.start < self.end:
        value = self.current
        self.current += self.prev
        self.prev = value
        self.start += 1
        return value


OBJ = IteratorFibonacci(0, 10)
print("****************** USING ISLICE *****************")
print(list(islice(OBJ, 0, 10)))
print("***************** NORMAL WORKING ****************")
print(list(OBJ))
