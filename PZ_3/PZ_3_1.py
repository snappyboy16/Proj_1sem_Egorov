# Даны два целых числа: A, B. Проверить истинность высказывания: “Ровно одно из чисел A и B нечетное”

a, b = input('Введите целое число A: '), input('Введите целое число B: ')

while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Некорректный ввод !')
        a = input('Введите целое число A: ')

while type(b) != int:  # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Некорректный ввод !')
        b = input('Введите целое число B: ')

if (a % 2) and (b % 2):
    print('False')  # выводим False, если 2 числа нечетных
elif (a % 2) + (b % 2) == 0:
    print('False')  # выводим False, если 2 числа четных
else:
    print('True')  # выводим True, если одно из чисел нечётное
