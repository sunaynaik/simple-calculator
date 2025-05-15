import math

def basic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operator")

def scientific_operation(func, x, y=None):
    if func == 'sin':
        return math.sin(math.radians(x))
    elif func == 'cos':
        return math.cos(math.radians(x))
    elif func == 'log':
        return math.log10(x)
    elif func == 'sqrt':
        return math.sqrt(x)
    elif func == 'factorial':
        return math.factorial(int(x))
    elif func == 'pow' and y is not None:
        return math.pow(x, y)
    else:
        raise ValueError("Invalid function or missing arguments")
