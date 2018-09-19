# coding: utf-8
# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). 
# Вывести на экран исходный и отсортированный массивы.

import random

def bubble(l):
	leng = len(l) - 1
	for i in range(leng):
	    for j in range(leng - i):
	        if a[j] < a[j+1]:
	            a[j], a[j+1] = a[j+1], a[j]
	print(a)


a = [random.randrange(-100,100) for _ in range(100)]

print('Исходный массив: ')
print(a)
print()
print('Отсортированный массив: ')
bubble(a)