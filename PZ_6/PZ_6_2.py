#  Дан список размера N. Найти количество его промежутков монотонности (то есть участков, на которых его элементы
#  возрастают или убывают).

from random import randint  # импорт библиотек

while True:  # обработка исключений
    try:
        a1, b1, n = int(input('Введите диапазон A: ')), int(input('Введите диапазон B: ')), \
                    int(input('Введите целое число N: '))  # ввод целых чисел
        break
    except ValueError:
        print('Некорректный ввод, попробуйте ещё раз!')

a = [randint(a1, b1) for _ in range(n)]  # список с циклом for
print(a)  # вывод A

k1, k2 = 0, 0
m = a[0]  # берем 1 элемент а
flag = True

for i in a[1:]:  # цикл for, где берем от 1 элемента
    if i < m:
        if flag:  # если Flag = True, добавляем k1 +=1
            flag = False
            k1 += 1
    else:
        flag = True

flag = True
m = a[0]

for i in a[1:]:
    if i < m:
        if flag:
            flag = False
            k2 += 1
    else:
        flag = True

k = k1 + k2  # складываем значения
print(k)
