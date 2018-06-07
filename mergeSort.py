#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'merging sort'

__author__ = 'lxp'

#《大话数据结构》407页

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

def mergeSort(L):
	MSort(L.r, L.r, 1, L.length - 1)

def MSort(SR, TR1, s, t):
	TR2 = [None] * len(SR)
	if s == t:
		TR1[s] = SR[s]
	else:
		m = int((s + t) / 2)
		MSort(SR, TR2, s, m)
		MSort(SR, TR2, m + 1, t)
		Merge(TR2, TR1, s, m, t)

def Merge(SR, TR, i, m, n):
	j = m + 1
	k = i
	while i <= m and j <= n:
		if SR[i] < SR[j]:
			TR[k] = SR[i]
			i = i + 1
		else:
			TR[k] = SR[j]
			j = j + 1
		k = k + 1
	if i <= m:
		for l in range(m - i + 1):
			TR[k + l] = SR[i + l]
	if j <= n:
		for l in range(n - j + 1):
			TR[k + l] = SR[j + l]



#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	mergeSort(L)
	L.show()

if __name__ == '__main__':
	test()
