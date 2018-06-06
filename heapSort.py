#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'heap sort'

__author__ = 'lxp'

#《大话数据结构》399页

class SqList(object):
	def __init__(self):
		self.r = [None]
		self.length = 0

	def show(self):
		a = True
		for l in self.r:
			if a == True:
				a = False
				continue
			print(l, ',', end = '')

def swap(L, i, j):
	temp = L.r[i]
	L.r[i] = L.r[j]
	L.r[j] = temp

def heapSort(L):
	for i in range(int(L.length / 2), 0, -1):
		heapAdjust(L, i, L.length)

	for i in range(L.length - 1, 1, -1):
		swap(L, 1, i)
		heapAdjust(L, 1, i - 1)

def heapAdjust(L, s, m):
	temp = L.r[s]
	j = 2 * s
	while j <= m:
		if j < m and L.r[j] < L.r[j + 1]:
			j = j + 1
		if temp >= L.r[j]:
			break
		L.r[s] = L.r[j]
		s = j
		j = j * 2
	L.r[s] = temp


#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	heapSort(L)
	L.show()

if __name__ == '__main__':
	test()
