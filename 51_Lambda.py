# Lambda function 
# ---
# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Syntax
# --
# lambda arguments: expression


multiply = lambda a, b: a*b
# print(multiply(4, 3))

# Lambda with print
tables = lambda a, b: print(f"{a} * {b} = {a*b}")
[tables(6, i) for i in range(1, 11)]