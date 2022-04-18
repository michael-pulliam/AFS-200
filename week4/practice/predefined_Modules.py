import math

#Returns the factorial of a number
print(math.factorial(5))

print(math.factorial(6))

# import math

myNumbers = [1,4,6,3,5,8]

#Returns the sum of all items in any iterable (tuples, arrays, lists, etc.).
print(math.fsum(myNumbers))

#Return a random element from a list
print(random.choice(myNumbers))

import random

a = 3
b = 8
#Return a random integer N such that a <= N <= b.
print(random.randint(a,b))