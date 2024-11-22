import math

def calculate_square_root(a):
    if a < 0:
        raise ValueError("The input value must be non-negative")
    return math.sqrt(a)