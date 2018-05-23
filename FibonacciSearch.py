#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Fibonacci search'

__author__ = 'lxp'

#《大话数据结构》303页

def Fbi(i):
	if i < 2:
		return i
	return Fbi(i - 1) + Fbi(i - 2)

def FibonacciSearch(a, key):
	n = len(a) - 1
	low = 0
	high = n
	k = 0
	while n > Fbi(k):
		k = k + 1
	for i in range(n, Fbi(k) - 1):
		a.append(a[-1])

	while low < high:
		mid = low + Fbi(k - 1) + 1
		if key < a[mid]:
			high = mid - 1
			k = k - 1
		elif key > a[mid]:
			low = mid + 1
			k = k - 2
		else:
			if mid < n:
				return mid
			else:
				return n

	if key == a[low]:
		return low

	return


#test
def test():
	key = int(input("请输入key"))
	L = [0, 1, 2, 3, 4]
	print(FibonacciSearch(L, key))
	return

if __name__ == '__main__':
	test()