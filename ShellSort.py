#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Shell sort'

__author__ = 'lxp'

#《大话数据结构》392页

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


def ShellSort(L):
	increment = L.length - 1
	#increment = int(increment / 3) + 1
	while True:
		increment = int(increment / 3) + 1
		for i in range(increment + 1, L.length):
			if L.r[i] < L.r[i - increment]:
				L.r[0] = L.r[i]
				j = i - increment
				while j > 0 and L.r[0] < L.r[j]:
					L.r[j + increment] = L.r[j]
					j = j - increment
				L.r[j + increment] = L.r[0]

		if increment == 1:
			break

#test
def test():
	L = SqList()
	for l in [9, 1, 5, 8, 3, 7, 4, 6, 2]:
		L.r.append(l)
	L.length = len(L.r)
	ShellSort(L)
	L.show()

if __name__ == '__main__':
	test()
