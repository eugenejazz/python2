# coding: utf-8
# 4. Определить, какое число в массиве встречается чаще всего.

import random
import sys

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)

def сountтum(a,b):
	count = 0
	for i in a:
		if i == b:
			count +=1
	return(count)

a = [random.randint(0, 100) for i in range(1000)]

d = {}
count = 0

# Подсчитываем сколько раз встречается каждое число и записываем результат в словарь:
for i in a:
	b = сountтum(a,i)
	d[i] = b

# Перебираем ключи словаря и находим число, которое встречается чаще других
maxnum = a[0]
for i in d:
	if d[i] > d[maxnum]:
		maxnum = i

# Перебираем словарь еще раз и находим какие числа встречаются столько же раз, как и найденное число. Результат записываем в список
m = []
maxfr = d[maxnum]
for i in d:
	if d[i] == maxfr:
		m.append(i)

print(f'Число или числа встречающиеся чаще всего: {m}')

print(f'Посмотрим, сколько памяти занимают объекты:')
print(f'а: {sys.getsizeof(a)}')
print(f'd: {sys.getsizeof(d)}')
print(f'maxnum: {sys.getsizeof(maxnum)}')
print(f'm: {sys.getsizeof(m)}')
print(f'maxfr: {sys.getsizeof(maxfr)}')
print(f'Заглянем внутрь словаря и списка:')
show_size(d)
show_size(m)
