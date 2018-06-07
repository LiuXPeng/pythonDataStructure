#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'merging sort'

__author__ = 'lxp'

#《大话数据结构》413页

import mergeSort

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

def mergeSort2(L):
	TR = [None] * L.length
	k = 1
	while k < L.length - 1:
		mergePass(L.r, TR, k, L.length - 1)
		k = 2 * k
		mergePass(TR, L.r, k, L.length - 1)
		k = 2 * k

def mergePass(SR, TR, s, n):
	i = 1
	while i <= n - 2 * s + 1:
		mergeSort.Merge(SR, TR, i, i + s - 1, i + 2 * s - 1)
		i = i + 2 * s
	if i < n - s + 1:
		mergeSort.Merge(SR, TR, i, i + s - 1, n)
	else:
		for j in range(i, n + 1):
			TR[j] = SR[j]



#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	mergeSort2(L)
	L.show()

if __name__ == '__main__':
	test()