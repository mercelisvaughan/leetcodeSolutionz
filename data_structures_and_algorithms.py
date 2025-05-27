print("hello world")

# code out the factorial algorithm
"""
we know we need base cases
we know it is a recursive problem
return the function

factorial is n example of recursion, what is does is multiple the number n by n-1 until it reaches 0
so, 4*3,3*2,2*1 then it stops
"""
def factorial(n):
    if n == 0:
        return 1
        # make a  calculation
    f = n*factorial(n-1)
    print("f = ", f)
    print("n = ", n)
    return f
factorial(4)
"""
f =  1
n =  1
f =  2
n =  2
f =  6
n =  3
f =  24
n =  4
"""

"""
backtracking is a type of recursion that is most useful for traversing tree structures
the following function is a recursive approach to generating all the possible permutations of a given string, s, of a
given length n:
"""
def bitStr(n, s):
    if n == 1: return s
    return [ digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]
print(bitStr(3,'abc'))