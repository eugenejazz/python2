# coding: utf-8
# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, 
# разработанных в рамках домашнего задания первых трех уроков.

# На примере:
# 3-4. Определить, какое число в массиве встречается чаще всего.

import random
import cProfile

# Первый вариант:

def main(n):
	def _countnum(a,b):
		count = 0
		for i in a:
			if i == b:
				count += 1
		return(count)

	a = [random.randint(0, 100) for i in range(n)]

	d = {}
	count = 0

	for i in a:
		b = _countnum(a,i)
		d[i] = b

	maxnum = a[0]
	for i in d:
		if d[i] > d[maxnum]:
			maxnum = i

	m = []
	maxfr = d[maxnum]
	for i in d:
		if d[i] == maxfr:
			m.append(i)


# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main(10)"
# 100 loops, best of 3: 27.7 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main(100)"
# 100 loops, best of 3: 639 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main(1000)"
# 100 loops, best of 3: 41.5 msec per loop

# cProfile.run('main(10)')
# 10    0.000    0.000    0.000    0.000 task04_1.py:8(_countnum)
# cProfile.run('main(1000)')
# 1000    0.050    0.000    0.050    0.000 task04_1.py:8(_countnum)
# cProfile.run('main(10000)')
# 10000    4.032    0.000    4.032    0.000 task04_1.py:8(_countnum)


def main_v2(n):
	a = [random.randint(0, 100) for i in range(n)]

	num = a[0]
	maxnum = 1
	for i in range(n - 1):
		m = 1
		for k in range(i + 1, n):
			if a[i] == a[k]:
				m += 1
		if m > maxnum:
			maxnum = m
			num = a[i]
	if maxnum > 1:
		pass
	else:
		pass

# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main_v2(10)"
# 100 loops, best of 3: 27.4 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main_v2(100)"
# 100 loops, best of 3: 662 usec per loop
# $ python3 -m timeit -n 100 -s "import task04_1" "task04_1.main_v2(1000)"
# 100 loops, best of 3: 54 msec per loop

# cProfile.run('main_v2(10)')
# 1    0.000    0.000    0.000    0.000 task04_1.py:53(main_v2)
# cProfile.run('main_v2(100)')
# 1    0.000    0.000    0.001    0.001 task04_1.py:53(main_v2)
# cProfile.run('main_v2(1000)')
# 1    0.054    0.054    0.057    0.057 task04_1.py:53(main_v2)


