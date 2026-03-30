"""

Keyword arguments:
argument -- description
Return: return_description

types of arguments:
positional arguments
keyword arguments
default arguments
"""

def greet(name, greeting="Hello"):
    """Greets a person with a given greeting.

    Keyword arguments:
    name -- the name of the person to greet
    greeting -- the greeting message (default is "Hello")
    Return: A greeting string.
    """
    return f"{greeting}, {name}!"

def factorial(n):
    """Calculates the factorial of a number using recursion.

    Keyword arguments:
    n -- the number to calculate the factorial for
    Return: The factorial of the number n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
    
def fibonacci(n):
    """Calculates the nth Fibonacci number using recursion.

    Keyword arguments:
    n -- the position in the Fibonacci sequence
    Return: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

"""
ARGS AND KWARGS

*args -- positional arguments this way you can pass a variable number of arguments to a function
**kwargs -- keyword arguments this way you can pass a variable number of keyword arguments to a function
"""

#example of *args
def sum_all(*args):
    """Sums all the positional arguments passed to the function.

    *args -- variable number of positional arguments
    Return: The sum of all arguments.
    """
    return sum(args)

#example of **kwargs
def print_info(**kwargs):
    """Prints the key-value pairs of the keyword arguments passed to the function.

    **kwargs -- variable number of keyword arguments
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(value)