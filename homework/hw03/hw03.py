HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'has_seven',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if k%10 ==7:
        return True 
    elif k==0:
        return False
    else:
        return has_seven(k//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # great example, be sure to review 
    # A tree recursion way of writing (cannot pass the tests because of time limits)
    if n==1:
        return 1
    elif n==2:
        return 2
    elif (n-1)%7==0 or has_seven(n-1):
        return pingpong(n-2)
    else:
       return 2*pingpong(n-1)-pingpong(n-2)


    def helper(k, i, increment):
        if n==k:
            return i
        if k%7==0 or has_seven(k):
            return helper(k+1, i-increment, -increment)
        return helper(k+1, i+increment, increment)
    return helper(1,1,1)
    # i is simialr to the value of result, increment and -increment measures the direction 



def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    """
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, term(k)), k + 1
    return total

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a)-street(b))+abs(avenue(a)-avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    result=[]
    for i in s:
        for x in range(i+1):
            if x*x==i:
                result += [x]
    return result 
    # Using list comprehension version (one line statement)
    return [round(n ** 0.5) for n in s if n == round(n ** 0.5) ** 2]
    # The filter condition: n== round(n**0.5)**2 ensures that n is a perfect square itself 
    # A very smart trick



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    from math import log2
    def helper(amount, k):
        if k==0:
            return 1
        elif k<0:
            return 0
        elif amount==0:
            return 1
        elif amount<0:
            return 0
        else:
            return helper(amount-2**k, k)+helper(amount, k-1)
    return helper(amount, int(log2(amount)))

    # A solution version without using log2
    def contrained_count(amount, smallest_coin):
        if amount==0:
            return 1
        if smallest_coin > amount:
            return 0
        without_coin =constrained_count(amount, smallest_coin * 2) # the number ways to constitute amount without using the smallest_coin
        with_cooin= contrained_count(amount-smallest_coin, smallest_coin)
        return without_coin + with_coin # the total number of ways could divide into two separate conditions 
    return contrained_count(amount,1 )
    


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n==1:
        print_move(start, end)
    elif n==2: # The case of n==2 is helpful to think about, but is not necessary in this case. 
        print_move(start, 6-start-end)
        print_move(start, end)
        print_move(6-start-end, end)
    else:
        move_stack(n-1, start, 6-start-end)
        move_stack(1, start, end)
        move_stack(n-1, 6-start-end, end)
       

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # Interesting Question: to solve the problem(giving the function a name), you need to pass it in as an argument to the lambda function 
    return (lambda f: lambda k: f(f, k))(lambda f,k : k if k==1 else mul (k, f(f, sub(k, 1))))
