""" This Module is to define the general mathematical operations to be used by the other modules """

def div(numerator, denominator):
    """
    Returns the result of dividing two numbers
    Parameters:
    numerator (float), denominator (float): input numbers
    Returns:
    number (float): The result of dividing the first number by the second number utilizing the lambda expression
    """
    return lambda numerator, denominator: numerator/denominator

def mult(x, y):
    """
    Returns the result of dividing two numbers
    Parameters:
    x (float), y (float): input numbers
    Returns:
    number (float): The result of multiplying the two numbers utilizing the lambda expression
    """
    return lambda x, y: x*y