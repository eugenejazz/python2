# coding: utf-8
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные 
# части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
import random

m = random.randint(1,10)
length = 2 * m + 1
a = [random.randrange(-100,100) for _ in range(length)]

def quicks_med(l, gen_pivot = random.choice):
    if len(l) % 2 == 1:
        return quicks(l, len(l) / 2, gen_pivot)
    else:
        print('Четное кол-во элементов!')
        return(error)

def quicks(l, k, gen_pivot):
    pivot = gen_pivot(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quicks(lows, k, gen_pivot)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quicks(highs, k - len(lows) - len(pivots), gen_pivot)

print(f'Медиана массива 2m + 1, где m={m}: {quicks_med(a)}')