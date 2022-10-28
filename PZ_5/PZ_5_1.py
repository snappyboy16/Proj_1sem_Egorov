# Составить фунцкию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т.д.
# Через сколько таких действий получится нуль ?

def func(n): # функция вычисления суммы числа
    summ = 0
    while n > 0:
        summ += n % 10
        n = n // 10
    return summ # возвращение суммы


num = int(input("Введите число: ")) # ввод числа
k = 0
while num > 0:
    num -= func(num)
    k += 1

print(f"Через {k} действий") # вывод действий