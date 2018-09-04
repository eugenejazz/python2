# coding: utf-8
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 100) for i in range(10)]

print(a)

max_n = a[0]
max_n_i = 0
min_n = a[0]
min_n_i = 0
count = 0

for i in a:
	if i > max_n:
		max_n = i
		max_n_i = count
	if i < min_n:
		min_n = i
		min_n_i = count
	count += 1

print(f'Максимальный элемент {max_n}, его индекс {max_n_i}')
print(f'Минимальный элемент {min_n}, его индекс {min_n_i}')

a[max_n_i] = min_n
a[min_n_i] = max_n

print(a)