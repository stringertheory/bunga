import collections


def shee(a: int, b: int) -> None:
    """This is a test of a documented function.

    Arguments:
        a: nothing
        b: nothing more
    """
    counter: collections.Counter = collections.Counter()
    counter["alice"] += 1
    counter["alice"] += 1
    counter["bob"] += 1
