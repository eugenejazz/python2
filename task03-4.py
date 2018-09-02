# coding: utf-8
# 4. Определить, какое число в массиве встречается чаще всего.

import random

def CountNum(a,b):
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
	b = CountNum(a,i)
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