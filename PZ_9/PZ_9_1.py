# Дан словарь с произвольным количеством элементов. Выяснить
# имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
# добавить его в словарь. Вывести на экран первоначальный словарь и измененный.

s = {'овощ': 'помидор', 'ягода': 'клубника'}  # словарь
print(s)  # вывод словаря
if 'фрукт' not in s:  # если нет в словаре, то добавляем
    s['фрукт'] = 'яблоко'
print(s)
