#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    """
    >>> 1 + 1
    2!
    """
    pass


def sub(x, y):
    """
    >>> sub(1, 100)
    100
    """
    return x + y


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
