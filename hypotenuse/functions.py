# addition
def addition(a, b):
    """This function returns a + b

    :param a: integer or float number
    :type a: int or float
    :param b: second integer or float number
    :type b: int or float
    :return: sum of the two inputs
    :rtype: int or float
    """
    if isinstance(a, str):
        return "Input should be integers or reals"
    elif isinstance(b, str):
        return "Input should be integers or reals"
    return a + b


# squared
def squared(a):
    """Returns square of input

    :param a: integer or float number
    :type a: int or float
    :return: integer or float number
    :rtype: int or float
    """
    return a * a


# sqroot
def sqroot(a):
    """Returns square root of input

    :param a: integer or float, greater than 0
    :type a: int or float
    :return: float
    :rtype: float
    """
    return a**0.5


# hypot
def hypot(a, b):
    """Function which returns the hypotenuse for right triangle with sides a,b

    :param a: integer or float
    :type a: int or float
    :param b: integer or float
    :type b: int or float
    :return: float
    :rtype: float
    """
    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)
    return sqroot(sumAB)
