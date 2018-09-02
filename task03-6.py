# coding: utf-8
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и 
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0, 100) for i in range(10)]

# Воспользуемся решением задачи 3 для поиска максимального и минимального элемента и их индексов
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

# Если максимальный и минимальный элементы расположены рядом - выведем 0
b = 0

# Если индекс минимального элемента больше максимального
if min_n_i > max_n_i:
	count = max_n_i+1
	# Если существует только один элемент между минимальным и максимальным, выведем его
	if min_n_i-1 == max_n_i+1:
		b = a[count]
	else:
		for _ in range(max_n_i, min_n_i-2):
			if count == max_n_i+1:
				b = a[count] + a[count+1]
				count += 1 
			else:
				b = b + a[count+1]
				count += 1 
# Если индекс минимального элемента меньше максимального
if min_n_i < max_n_i:
	count = min_n_i+1
	# Если существует только один элемент между минимальным и максимальным, выведем его
	if min_n_i+1 == max_n_i-1:
		b = a[count]
	else:
		for _ in range(min_n_i, max_n_i-2):
			if count == min_n_i+1:
				b = a[count] + a[count+1]
				count += 1 
			else:
				b = b + a[count+1]
				count += 1 

print(f'Сумма элементов между минимальным и максимальным элементами равна {b}')
