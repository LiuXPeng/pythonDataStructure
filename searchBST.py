#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'binary sort tree'

__author__ = 'lxp'

#《大话数据结构》316页，基于python语言特点，重构了一下，和书上有些差异

class BiTNode(object):
	def __init__(self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None


def searchBST(T, key, f = None):
	if not T:
		return False, f
	elif key == T.data:
		return True, T
	elif key < T.data:
		return searchBST(T.lchild, key, T)
	else:
		return searchBST(T.rchild, key, T)

def insertBst(T, key):
	is_in, f = searchBST(T, key)
	if not is_in:
		s = BiTNode(key)
		if not f:
			T = s
		elif key < f.data:
			f.lchild = s
		else:
			f.rchild = s
		return T
	else:
		print("已含有")
		return T

#test
def test():
	L = [23, 24, 34, 1, 3, 7, 8, 8, 9, 0]
	T = None
	for l in L:
		T = insertBst(T, l)
	is_in, f = searchBST(T, int(input("要查找的数")))
	if is_in:
		print(f.data)
	else:
		print("没有")
	return

if __name__ == '__main__':
	test()
