# Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y, а в переменную
# Y - максимальное из этих значений (X и Y - вещественные параметры, являющиеся одновременно вводными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из данных чисел A, B, C, D.


def minmax(x: float, y: float):
    if x > y:
        x, y = y, x  # x и y меняются местами
        return x, y
    return x, y


a, b, c, d = input("Введите вещественное число A: "), input("Введите вещественное число B: "),\
             input("Введите вещественное число C: "), input("Введите вещественное число D: ")  # ввод вещественного #
# числа

while type(a) != float or type(b) != float or type(c) != float or type(d) != float:  # обработка исключений
    if type(a) != float:
        try:
            a = float(a)
        except ValueError:
            print('Некорректный ввод!')
            a = input("Введите вещественное число A: ")
    if type(b) != float:
        try:
            b = float(b)
        except ValueError:
            print('Некорректный ввод!')
            b = input("Введите вещественное число B: ")
    if type(c) != float:
        try:
            c = float(c)
        except ValueError:
            print('Некорректный ввод!')
            c = input("Введите вещественное число C: ")
    if type(d) != float:
        try:
            d = float(d)
        except ValueError:
            print('Некорректный ввод!')
            d = input("Введите вещественное число D: ")

a, b = minmax(a, b)  # 1 вызов функции
c, d = minmax(c, d)  # 2 вызов функции
a, c = minmax(a, c)  # 3 вызов функции
b, d = minmax(b, d)  # 4 вызов функции

print(f"Минимальное значение: {a}\nМаксимальное значение: {d}")  # вывод минимального и максимального значения
