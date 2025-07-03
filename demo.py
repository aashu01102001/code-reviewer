def add(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "division by zero error"
    return result
