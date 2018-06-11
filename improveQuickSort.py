#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'improve quick sort'

__author__ = 'lxp'

#《大话数据结构》424页

import insertSort

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

def quickSort(L):
	qSort(L, 1, L.length - 1)

def qSort(L, low, high):
	if high - low > 5:#自定义阈值
		while low < high:
			pivot = partition(L, low, high)
			qSort(L, low, pivot - 1)
			low = pivot + 1
	else:
		insertSort.insertSort(L)


def partition(L, low, high):
	m = int(low + (low + high) / 2)
	if L.r[high] < m:
		swap(L, high, m)
	if L.r[low] < m:
		swap(L, low, m)
	pivotkey = L.r[low]
	L.r[0] = pivotkey
	while low < high:
		while low < high and L.r[high] >= pivotkey:
			high = high - 1
		L.r[low] = L.r[high]
		while low < high and L.r[low] <= pivotkey:
			low = low + 1
		L.r[high] = L.r[low]
	L.r[low] = L.r[0]
	return low


#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	quickSort(L)
	L.show()

if __name__ == '__main__':
	test()