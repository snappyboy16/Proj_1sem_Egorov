import random


def listing(a, b):  # составление списка со случайными числами
    x = 0
    s = []
    while x != a:
        s.append(random.randrange(0, b))  # добавляем в конец списка
        x += 1
    return s


while True:  # обработка исключений
    try:
        n, z = int(input('Введите количество чисел спиcка: ')), \
               int(input('Список сформируется от 0 и до: '))  # ввод целого числа
        break
    except ValueError:
        print('Неккоректный ввод, попробуйте ещё раз !')

lst = listing(n, z)

print(f'Исходный список: {lst}')
lst.pop(-1)  # удаление последнего элемента
lst[0] = 0  # замена 1 элемента на 0
print(f'Конечный список: {lst}')  # вывод конечного списка
