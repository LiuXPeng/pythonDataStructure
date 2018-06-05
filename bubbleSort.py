#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'bubble sort'

__author__ = 'lxp'

#《大话数据结构》379页

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

def bubbleSort0(L):
	for i in range(1, L.length):
		for j in range(i + 1, L.length):
			if L.r[i] > L.r[j]:
				swap(L, i, j)

def bubbleSort(L):
	for i in range(1, L.length):
		for j in range(L.length - 2, i - 1, -1):
			if L.r[j] > L.r[j + 1]:
				swap(L, j, j + 1)

def bubbleSort2(L):
	flag = True
	for i in range(1, L.length):
		if flag == False:
			break
		flag = False
		for j in range(L.length - 2, i - 1, -1):
			if L.r[j] > L.r[j + 1]:
				swap(L, j, j + 1)
				flag = True

#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	bubbleSort0(L)
	L.show()

def test1():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	bubbleSort(L)

def test2():
	L = SqList()
	for l in [2, 1, 3, 4, 5, 6, 7, 8]:
		L.r.append(l)
	L.length = len(L.r)
	bubbleSort2(L)

	L.show()
if __name__ == '__main__':
	test2()
