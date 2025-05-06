"""
Вычислить площадь треугольника по трем сторонам или по двум сторонам и углу между ними,
значения в нужных единицах измерения вводит пользователь.
"""


from calc import calc_trem, calc_ugl
from check_input import check_num


def input_num(str_for_input: str) -> float:
    num = input(str_for_input)
    if check_num(num):
        result = float(num)
    else:
        print("Вы ввели не число, повторите ввод \n")
        result = input_num(str_for_input)

    return result


def main():
    print("Программа треугольника по трем сторонам или по двум сторонам и углу между ними, значения в нужных единицах измерения вводит пользователь.")
    flag = True
    while flag:
        a = input_num("Введите первую сторону: ")
        if a > 0 and a != float("inf"):
            flag = False
        elif a <= 0:
            print("Введите число больше")
        else:
            print("Вы ввели слишком большое число")
    flag = True
    while flag:
        b = input_num("Введите вторую сторону: ")
        if b > 0 and b != float("inf"):
            flag = False
        elif b <= 0:
            print("Введите число больше")
        else:
            print("Вы ввели слишком большое число")
    flagm = True
    while flagm:
        dim_okr = int(input("Вычислить треугольник по 1 - трем сторонам или 2 - углу между ними: "))
        if dim_okr == 1:
            flagm = True
            while flagm:
                c = input_num("Введите третью сторону: ")
                if c > 0 and c != float("inf"):
                    flagm = False
                elif c <= 0:
                    print("Введите число больше")
                else:
                    print("Вы ввели слишком большое число")
        elif dim_okr == 2:
            flagm = True
            while flagm:
                c = input_num("Введите угол между ними: ")
                if c > 0 and c != float("inf"):
                    flagm = False
                elif c <= 0:
                    print("Введите число больше")
                else:
                    print("Вы ввели слишком большое число")

    err = "Сторона больше суммы других двух сторон"
    if dim_okr == 1:
        if a + b < c:
            print(err)
        elif a + c < b:
            print(err)
        elif c + b < a:
            print(err)
        else:
            result = calc_trem(a, b, c)
            if result != False and result != float("inf"):
                print(f"Площадь треугольника по трем сторонам: {result:.4f}")
            else:
                print("Ошибка при вычислении площади.")
    elif dim_okr == 2:
        result = calc_ugl(a, b, c)
        if result != False and result != float("inf"):
            print(f"Площадь треугольника по углу между двумя сторонами: {result:.4f}")
        else:
            print("Ошибка при вычислении площади.")

    flag = True
    while flag:
        dalsh = input("Для продолжения работы введите 1, для выхода 0: ")
        if dalsh == "1":
            flag = False
            main()
        elif dalsh != "0":
            print("Не верный ввод")
        else:
            flag = False


if __name__ == '__main__':
    main()