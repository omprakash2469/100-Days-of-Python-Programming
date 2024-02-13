"""
Recursion 
----
Recursion is the process of defining something in terms of itself.

In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
"""

def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

    
print(factorial(4)) # Factorial of 5 is 120


# Factorial(0) == 1 ( by default )
# Factorial of 5 => 5 * 4 * 3 * 2 * 1 = 120
# Factorial of 4 => 4 * 3 * 2 * 1 = 24
