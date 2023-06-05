import collections


def shee():
    c = collections.Counter()
    c["alice"] += 1
    c["alice"] += 1
    c["bob"] += 1
    return c.total()
