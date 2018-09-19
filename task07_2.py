# coding: utf-8
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random

def merge(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

a = [random.uniform(0,49) for _ in range(100)]

print('Исходный массив: ')
print(a)
print()
merge(a)
print('Отсортированный массив: ')
print(a)
