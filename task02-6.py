# coding: utf-8
# 6. В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или меньше 
# загаданного введенное пользователем число. Если за 10 попыток число 
# не отгадано, то вывести его.

import random

a = random.randint(0, 100)
n = 0

while n < 10:
	b = int(input("Введите число: "))
	if b != a:
		print("Неверно")
		n += 1
	else:
		print("Угадали")
		break

print(a)