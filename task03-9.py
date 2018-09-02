# coding: utf-8
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
M = 8
N = 4
a = [[random.randrange(0,1000) for _ in range(M)] for _ in range(N)]

for i in range(N):
	print(a[i])

max_n = -1
for i in range(M):
	min_n = 1000
	for j in range(N):
		# print(f'a[j][i]= {a[j][i]}')
		if a[j][i] < min_n:
			min_n = a[j][i]
			# print(f'min_n= {min_n}')
			# print(f'max_n= {max_n}')
	if min_n > max_n:
		max_n = min_n

print(f'Максимальный элемент среди минимальных: {max_n}')