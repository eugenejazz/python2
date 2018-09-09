# coding: utf-8
# 2. Написать два алгоритма нахождения i-го по счёту простого числа. 
# Первый - использовать алгоритм решето Эратосфена. 
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile

def simplesieve(n,c):
	sieve = [i for i in range(n)]
	sieve[1] = 0

	for i in range(2, n):
		if sieve[i] != 0:
			j = i * 2
			while j < n:
				sieve[j] = 0
				j += i
	res = [i for i in sieve if i != 0]
	number = res[c - 1]

# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.simplesieve(100,20)"
# 100 loops, best of 3: 35.4 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.simplesieve(1000,20)"
# 100 loops, best of 3: 382 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.simplesieve(10000,20)"
# 100 loops, best of 3: 4.38 msec per loop

# cProfile.run('simplesieve(100,20)')
# 1    0.000    0.000    0.000    0.000 task04_2.py:8(simplesieve)
# cProfile.run('simplesieve(1000,20)')
# 1    0.000    0.000    0.000    0.000 task04_2.py:8(simplesieve)
# cProfile.run('simplesieve(10000,20)')
# 1    0.004    0.004    0.005    0.005 task04_2.py:8(simplesieve)

def withoutsieve(n,c):
	res = []
	for i in range(2, n+1):
	    for j in range(2, i):
	        if i % j == 0:
	            # если делитель найден, число не простое.
	            break
	    else:
	        res.append(i)
	number = res[c - 1]

# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.withoutsieve(100,20)"
# 100 loops, best of 3: 113 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.withoutsieve(1000,20)"
# 100 loops, best of 3: 6.08 msec per loop
# $ python3 -m timeit -n 100 -s "import task04_2" "task04_2.withoutsieve(10000,20)"
# 100 loops, best of 3: 573 msec per loop

# cProfile.run('withoutsieve(100,20)')
# 1    0.000    0.000    0.000    0.000 task04_2.py:35(withoutsieve)
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('withoutsieve(1000,20)')
# 1    0.006    0.006    0.006    0.006 task04_2.py:35(withoutsieve)
# 168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('withoutsieve(10000,20)')
# 1    0.531    0.531    0.532    0.532 task04_2.py:35(withoutsieve)
# 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
