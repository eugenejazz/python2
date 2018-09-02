# coding: utf-8

# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def checkeven(x):
	if (int(x) % 2) == 0:
		return 1
	else:
		return 0

def checkodd(x):
	if (int(x) % 2) == 0:
		return 0
	else:
		return 1

a = str(input("Введите число: "))
even=0
odd=0

for i in a:
	even = even + checkeven(i)
	odd = odd + checkodd(i)

print(f'Четные: {even}')
print(f'Нечетные: {odd}')