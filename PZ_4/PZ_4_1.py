# Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2

n = input('Введите число N: ')

while type(n) != int: # обработчик исключений
    try:
        n = int(n)
    except ValueError:
        print('Неккоректный ввод!')
        n = input('Введите число N: ')

x = n ** 2
i = 0
while i in range(n): # цикл while с последовательностью до n
    i += 1
    x = x + ((n + i) ** 2)
print(f'Сумма N = {x}')