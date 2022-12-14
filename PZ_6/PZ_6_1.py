# Дан список размера N и целое число K (1<K<N). Вывести элементы список с порядковыми номерами, кратными K: Ak, A2*k,
# A3*k,... .Условный оператор не использовать.

from random import randint  # импорты библиотек рандом

while True:  # обработка исключений
    try:
        a1, b1, n, k = int(input('Введите диапазон целого числа A: ')), int(input('Введите диапазон целого числа B: ')), \
                       int(input('Введите последовательность чисел N: ')), int(input('Введите целое число K: '))
        # ввод чисел
        break
    except ValueError:
        print('Некорректный ввод, попробуйте ещё раз!')

a = [randint(a1, b1) for i in range(n)]  # список, внутри цикл for
print(a)
for i in a[k - 1::k]:
    print(i)
