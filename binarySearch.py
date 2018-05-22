#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'binary search'

__author__ = 'lxp'

#《大话数据结构》299页

def binarySearch(a, key):
	n = len(a)
	low = 0
	high = n - 1

	while low < high:
		mid = int((low + high) / 2)
		if (key < a[mid]):
			high = mid - 1
		elif key > a[mid]:
			low = mid + 1
		else:
			return mid
	if a[low] == key:
		return low
	return 


#test
def test():
	key = int(input("请输入key"))
	L = [0,1,2,3,4,5,6,7]
	print(binarySearch(L, key))
	return

if __name__ == '__main__':
	test()