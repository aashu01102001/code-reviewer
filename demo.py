def add(a, b):
    """
    Performs safe division of a by b.
    
    Parameters:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: result of division if valid
        str: error message if invalid
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Invalid input types"
    return result
