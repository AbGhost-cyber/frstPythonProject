def is_numeric(*args):
    for x in args:
        return isinstance(x, (int, float))
