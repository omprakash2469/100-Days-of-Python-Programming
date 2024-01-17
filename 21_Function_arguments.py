"""
There are four types of arguments we can pass to function
---

1. Default arguments
2. Variable length arguments
3. Keyword arguments
4. Required arguments

"""

# ========================================
# 1. Default arguments
# ========================================
def greet(name, msg="Hello!"):
    """
    msg have a default argument. It will ignore default argument if we pass a value to the function
    """
    print(f"{msg} {name}")

greet("Omprakash") # call with default argument
greet("Omprakash", "How are you?") # call by passing argument



# ========================================
# 2. Required arguments
# ========================================
greet(name="Omprakash") # `name` is the required argument for this function


# ========================================
# 3. Keyword arguments
# ========================================
# You have to pass arguments in the order in which they are in the function, or else you have to pass the argument with assigning the parameter name while calling the functin

# greet("Omprakash") # Passing arguments in order
# greet(name="Omprakash", msg="How are you?") # Passing by argument name


# ========================================
# 4. Variable length arguments
# ========================================
def newGreet(*args, **kwargs):
    print(args) # Provides a tuple of the arguments passed to the function
    print(kwargs) # Provides a dictionary of the key and value pairs passed in the dictionary

newGreet("New Name", first_name="omprakash", last_name = "prajapati")
