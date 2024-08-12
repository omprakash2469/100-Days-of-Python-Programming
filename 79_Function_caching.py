# Function Caching 
"""
Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.
"""


from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def get_number(x):
    sleep(5)
    return x * 99999


print(get_number(3))