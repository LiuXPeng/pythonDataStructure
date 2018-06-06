#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'simple selection sort'

__author__ = 'lxp'

#《大话数据结构》384页

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

def selectSort(L):
	for i in range(1, L.length):
		min = i
		for j in range(i + 1, L.length):
			if L.r[min] > L.r[j]:
				min = j
		if min != i:
			swap(L, i, min)

#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	selectSort(L)
	L.show()

if __name__ == '__main__':
	test()
