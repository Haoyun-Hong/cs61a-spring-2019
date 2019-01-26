""" Homework 1: Control """

# Q1
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# Q2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a,b,c) * max(a, b, c)+ (a+b+c-max(a, b, c)-min(a, b,c))*(a+b+c-max(a, b, c)-min(a, b,c))

# Q3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i=n-1
    while i >0 :
        if n%i ==0:
            return i
        i -=1

# Q4
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return 1==2

def t():
    "*** YOUR CODE HERE ***"
    print(1)

def f():
    "*** YOUR CODE HERE ***"
    print (2)

#very crucial example: be sure to review using python tutor: 
#http://pythontutor.com/composingprograms.html#code=def%20if_function%28condition,%20true_result,%20false_result%29%3A%0A%20%20%20%20if%20condition%3A%0A%20%20%20%20%20%20%20%20return%20true_result%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20false_result%20%0A%20%20%20%20%0Adef%20with_if_function%28%29%3A%0A%20%20%20%20return%20if_function%28c%28%29,%20t%28%29,%20f%28%29%29%0A%0Adef%20c%28%29%3A%0A%20%20%20%20return%201%3D%3D2%0A%0Adef%20t%28%29%3A%0A%20%20%20%20return%20print%281%29%0A%0Adef%20f%28%29%3A%0A%20%20%20%20return%20print%20%282%29%0A%0Adef%20with_if_statement%28%29%3A%0A%20%20%20%20if%20c%28%29%3A%0A%20%20%20%20%20%20%20%20return%20t%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20f%28%29%0A%0Awith_if_function%28%29%0Awith_if_statement%28%29&cumulative=true&curInstr=34&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D


# Q5
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

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
    """
    "*** YOUR CODE HERE ***"
    count=0
    while n is not 1:
        if n%2 ==0: 
            print(n)
            n =n //2
            count +=1
        else:
            print(n)
            n=3*n+1
            count+=1
    print(n)
    return count+1
    