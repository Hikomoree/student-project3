import math


def check_num(text: str) -> bool:
    result = True
    try:
        num = int(text)
    except ValueError:
        result = False

    return result


def check_calc_trem(a: float, b: float, c: float) -> bool:
    result = True
    try:
        p = (a * b * c) / 2
        rest = math.sqrt(p * (p - a) * (p - b) * (p - c))
    except:
        result = False

    return result


def check_calc_ugl(a: float, b: float, c: float) -> bool:
    result = True
    try:
        rest = (a * b * math.sin(c)) / 2
    except:
        result = False

    return result