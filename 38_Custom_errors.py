# Raising custom errors
# In python, we can raise custom errors by using the raise keyword.

a = int(input("Enter a number: "))
if (a<5 or a>9):
    raise ValueError("Please enter an integer between 5 to 9!")


# Define custom error
class KeywordNotFound(Exception):
    pass
    
x, y = 12, 12
if (x == y):
    # raise custom error
    raise KeywordNotFound("Keyword is not found")