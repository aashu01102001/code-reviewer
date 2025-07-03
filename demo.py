def add(a, b):
    if b == 0:
        raise ValueError("b cannot be zero for division")
    return round(a / b, 2)  # round to 2 decimal places
