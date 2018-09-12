# coding: utf-8
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

import sys

a = [i for i in range(2,100)]
b = [i for i in range(2,10)]

def checkformultiplicity(a,b):
	count = 0
	for i in a:
		if i % b == 0:
			count += 1
	return(count)

print(f'В диапазоне чисел от {a[0]} до {a[-1]}:')

for i in b:
	print(f'{checkformultiplicity(a,i)} будут кратны {i}')

print(f'Посмотрим, сколько памяти занимают a и b:')
print(f'а: {sys.getsizeof(a)}')
print(f'b: {sys.getsizeof(b)}')

print(f'Поменяем тип объекта b на кортеж:')

del a
del b

a = [i for i in range(2,100)]
b = (i for i in range(2,10))

for i in b:
	print(f'{checkformultiplicity(a,i)} будут кратны {i}')


print(f'Посмотрим, сколько теперь памяти занимают a и b:')
print(f'а: {sys.getsizeof(a)}')
print(f'b: {sys.getsizeof(b)}')

print(f'Использование кортежей сокращает использование памяти')