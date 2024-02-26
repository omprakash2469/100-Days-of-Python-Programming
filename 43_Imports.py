"""

How importing in python works
---
Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

"""


"""
from keyword
---
You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write.
"""
from math import sqrt


"""
The dir function
---
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
"""
import math
print(dir(math))
