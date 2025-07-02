def add(a, b):
    """
    Performs safe division of a by b.
    Returns:
        float: result of division if valid
        str: error message if invalid
    """
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
