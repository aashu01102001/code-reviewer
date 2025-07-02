def add(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
