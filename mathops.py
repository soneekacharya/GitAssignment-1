def add(a, b):
    """
    Add two numbers and return the result.

    This function takes two numeric values, 'a' and 'b', and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of 'a' and 'b'.
    """
    return a + b

def sub(a, b):
    """
    Subtract two numbers and return the result.

    This function takes two numeric values, 'a' and 'b', and returns their difference.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference of 'a' and 'b'.
    """
    return a - b

def mul(a, b):
    """
    Multiply two numbers and return the result.

    This function takes two numeric values, 'a' and 'b', and returns their product.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of 'a' and 'b'.
    """
    return a * b

def div(a, b):
    """
    Divide 'a' by 'b' and return the result.

    This function takes two numeric values, 'a' (dividend) and 'b' (divisor), and returns the result
    of dividing 'a' by 'b'.

    Args:
        a (int or float): The number to be divided.
        b (int or float): The number to divide by.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If 'b' is 0.
    """
    return a / b

print("Sum is:", add(5,10))
print("Difference is:", sub(15,10))
print("Product is:", mul(5,10))
print("Quotient is:", div(15,3))