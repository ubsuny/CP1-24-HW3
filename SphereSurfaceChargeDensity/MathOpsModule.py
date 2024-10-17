""" This Module is to define the general mathematical operations to be used by the other modules """

def div(numerator, denominator):
    """
    Returns the result of dividing two numbers
    Parameters:
    numerator, denominator: input numbers
    Returns:
    number: The result of dividing the first number by the second number utilizing the lambda expression
    """
    Div = lambda x, y: x/y
    return Div(numerator, denominator)

def mult(x, y):
    """
    Returns the result of dividing two numbers
    Parameters:
    x, y: input numbers
    Returns:
    number: The result of multiplying the two numbers utilizing the lambda expression
    """
    Mult = lambda xx, yy: xx*yy
    return Mult(x, y)