from math import tan, pi


def area_poly(n, s):
    """
    :param n: int, number of sides of a polygon
    :param s: num, length of the boundary of the polygon
    :return: the area of the polygon
    """
    return (0.25 * n * s ** 2)/(tan(pi/n))


def perimeter_poly(n, s):
    """
    :param n: (int) number of sides of a polygon
    :param s: (int, float) length of the boundary of the polygon
    :return: (int, float) the perimeter of the regular polygon
    """
    return n * s


def polysum(n, s):
    """
    :param n: (int) number of sides of a polygon
    :param s: (int, float) length of the boundary of the regular polygon
    :return: (int, float) the sum of the area and the square of the perimeter of a regular polygon
    """
    return round(area_poly(n, s) + perimeter_poly(n, s) ** 2, 4)
