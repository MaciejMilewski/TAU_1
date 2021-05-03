import numbers
import math


def matura_logarithm(x):
    """ Logarithm of (x^3 - x^2) with base (2*x - 3) / (x + 3) """
    if isinstance(x, numbers.Number) is not True:
        result = "Error: " + str(x) + " is not a number"
    elif x <= 1.5 or x == 6:
        result = None
    elif x > 1.5 and x != 6:
        result = math.log(x*x*x - x*x, (2*x - 3) / (x + 3))
    else:
        result = "Unexpected"
    return result