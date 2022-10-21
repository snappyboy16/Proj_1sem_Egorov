# Дано целое число N (> 1). Найти наибольшее целое число K, ри котором выполняется неравенство 3k < N.

n = input('Введите число N: ')

while type(n) != int: # обработчик исключений
    try:
        n = int(n)
    except ValueError:
        print('Некорректный ввод!')
        n = input('Введите число N: ')

k = 0
while 3 ** k < n: #цикл while
    k += 1
print(f'K = {k}')