"""
Docstrings
---

Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
"""


# Example - 1
def total(a, b):
    """ Returns the sum of a and b """
    sum = a + b
    print(sum)
    return sum

total(45, 23)


# Example - 2
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    
    Parameters
    -------
    num1 : int
        First number to add.

    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

print(add(6534, 8923))

"""
Python Comments vs Docstrings
-----------------------------

Python Comments
---
Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

Python docstrings
---
As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

"""

# Doc Attribute
print(total.__doc__) # Returns the doc string of the function


"""
PEP 8
---------------
PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

"""