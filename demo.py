def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "Invalid input"
