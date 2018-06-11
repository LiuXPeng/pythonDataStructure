#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'quick sort'

__author__ = 'lxp'

#《大话数据结构》417页

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
	if low < high:
		pivot = partition(L, low, high)
		qSort(L, low, pivot - 1)
		qSort(L, pivot + 1, high)

def partition(L, low, high):
	pivotkey = L.r[low]
	while low < high:
		while low < high and L.r[high] >= pivotkey:
			high = high - 1
		swap(L, low, high)
		while low < high and L.r[low] <= pivotkey:
			low = low + 1
		swap(L, low, high)
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