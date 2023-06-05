import collections


def shee(a: int, b: int) -> int:
    """This is a test of a documented function.

    Arguments:
        a: nothing
        b: nothing more
    """
    counter: collections.Counter = collections.Counter()
    counter["alice"] += 1
    counter["alice"] += 1
    counter["bob"] += 1
    return counter.total()
