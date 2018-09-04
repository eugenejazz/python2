# coding: utf-8
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for i in range(10)]
print(a)

alen = len(a)
maxnum = 0
index = -1

for i in range(0,alen):
	if index == -1 and a[i] < 0:
		index = i
	elif index != -1 and a[i] < 0 and a[i] > a[index]:
		index = i

if index == -1:
	print(f'Нет орицательных элементов')
else:
	print(f'Максимальный отрицательный элемент = {a[index]}')