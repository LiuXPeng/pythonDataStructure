#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'straight insertion sort'

__author__ = 'lxp'

#《大话数据结构》386页

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

def insertSort(L):
	for i in range(2, L.length):
		if L.r[i] < L.r[i - 1]:
			L.r[0] = L.r[i]
			j = i - 1
			while L.r[j] > L.r[0]:
				L.r[j + 1] = L.r[j]
				j = j - 1
			L.r[j + 1] = L.r[0]

#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	insertSort(L)
	L.show()

if __name__ == '__main__':
	test()