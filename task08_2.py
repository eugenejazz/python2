# coding: utf-8
# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

import heapq
from collections import Counter 
from collections import namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


s = input("Введите строку для кодирования:")

h = []

for ch, fr in Counter(s).items(): 
	h.append((fr, len(h), Leaf(ch)))
heapq.heapify(h)
count = len(h)
while len(h) > 1:
	fr1, c1, left = heapq.heappop(h)
	fr2, c2, right = heapq.heappop(h)
	heapq.heappush(h, (fr1 + fr2, count, Node(left, right)))
	count += 1

code = {}

if h:
	[(_fr, _count, root)] = h
	root.walk(code, "")
print(f'Закодированная строка: ')

for i in s:
	print(code[i], end="")

print()






