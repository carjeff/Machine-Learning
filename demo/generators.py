import random

def randFloat(low: float, high: float):
    def next(max):
        count = 0
        while True:
            if max == count:
                break
            yield low + random.random() * (high - low)
            count += 1
    return next