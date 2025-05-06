import math

from check_input import check_calc_trem, check_calc_ugl


def calc_trem(a: float, b: float, c:float) -> float:

    if check_calc_trem(a, b, c):
        p = (a * b * c) / 2
        result = math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        result = False


    return result


def calc_ugl(a: float, b: float, c:float) -> float:
    if check_calc_ugl(a, b, c):
        result = (a * b * math.sin(c)) / 2
    else:
        result = False


    return result