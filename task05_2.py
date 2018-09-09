# coding: utf-8
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, 
# элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F. 
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. 
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# 

# Успел только сложение :( Интересно посмотреть корректный вариант решения, думаю мой не совсем то, что требовалось

import collections

def check_len(a,b):
	lena = len(a)
	lenb = len(b)
	if lena > lenb:
		return lena
	if lenb > lena:
		return lenb
	if lena == lenb:
		return lena

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
z =[]
for i in d.keys():      
    z.append((d[i],i))
rd=dict(z) 

a = collections.deque(input('Введите первое число: '))
b = collections.deque(input('Введите второе число: '))

def hex_addition(a,b):
	maxlen = check_len(a,b)

	while len(a) < maxlen:
		a.appendleft(0)

	while len(b) < maxlen:
		b.appendleft(0)

	# Сложение

	a.reverse()
	b.reverse()

	res = 0
	summa = collections.deque()

	for i,k in enumerate(a):
		x = str(a[i])
		y = str(b[i])
		s = d[x] + d[y] + res
		if s > 16:
			s = s - 16
			res = 1
			result = rd[s]
			summa.append(result)
		elif s < 16:
			res = 0
			result = rd[s]
			summa.append(result)
		elif s == 16:
			s = s - 16
			res = 1
			result = rd[s]
			summa.append(result)

	if res == 1:
		summa.append(res)

	summa.reverse()
	return(summa)


summa = hex_addition(a,b)

print('Сумма чисел: ')
for i in summa:
	print(i, end='')
print()
