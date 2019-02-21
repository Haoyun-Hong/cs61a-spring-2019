""" Lab 04 Optional Questions """

from lab04 import *


this_file = __file__


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'hailstone',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(n, k):
        print(n)
        if n==1:
            return k
        else:
            if n%2==0:
                return helper(n//2, k+1)
            else:
                return helper(3*n+1, k+1)
    return helper(n, 1)