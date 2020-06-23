"""Main module."""


def add(x: float, y: float) -> float:
    """Add two numbers

    Arguments
    ---------
    x : float
        First number
    y : float
        Second number.

    Returns
    -------
    float
        The sum of x and y
    """
    return float(x + y)


def subtract(x: float, y: float) -> float:
    """Subtract two numbers

    Arguments
    ---------
    x : float
        First number
    y : float
        Second number.

    Returns
    -------
    float
        x - y
    """
    return float(x - y)


def divide(x: float, y: float) -> float:
    """Divide :math:`x` by :math:`y`

    Arguments
    ---------
    x : float
        First number
    y : float
        Second number.

    Raises
    ------
    ZeroDivisionError:
        If the denominator is zero

    Returns
    -------
    float
        x / y
    """
    if abs(y) < 1e-12:
        raise ZeroDivisionError("Cannot divede by zero")
    return x / y
