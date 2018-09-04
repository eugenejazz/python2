# coding: utf-8
# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

a = [random.randint(0, 100) for i in range(10)]

# Воспользуемся решением задачи 3 для поиска максимального и минимального элемента и их индексов

min_n = a[0]
min_n_i = 0
count = 0

for i in a:
	if i < min_n:
		min_n = i
		min_n_i = count
	count += 1

# Запишем минимальный элемент в список и удалим его из массива
b = [a[min_n_i]]
a.pop(min_n_i)

# Повторим алгоритм поиска и выведем получившийся список
min_n = a[0]
min_n_i = 0
count = 0

for i in a:
	if i < min_n:
		min_n = i
		min_n_i = count
	count += 1

b.append(a[min_n_i])

print(f'Два наименьших элемента массива: {b}')