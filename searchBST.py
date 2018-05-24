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

def deleteBST(T, key):
	p = T
	f= None

	try:
		while p.data != key:
			f = p
			if p.data > key:
				p = p.lchild
			else:
				p = p.rchild
	except:
		print("不含此点")
		return T

	if f == None:
		if p.rchild == None:
			T = T.lchild#这里只能用T，地址运算
			return T
		elif p.lchild == None:
			T = T.rchild
			return T

	if p.rchild == None:
		if f.data > key:
			f.lchild = p.lchild
		else:
			f.rchild = p.lchild
	elif p.lchild == None:
		p.data = p.rchild.data
		p.lchild = p.rchild.lchild
		p.rchild = p.rchild.rchild
	else:
		q = p
		s = p.lchild
		while s.rchild:
			q = s
			s = s.rchild
		p.data = s.data
		if q != p:
			q.rchild = s.lchild
		else:
			q.lchild = s.lchild	

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
	T = deleteBST(T, int(input("请输入要删除的数")))
	is_in, f = searchBST(T, int(input("要查找的数")))
	if is_in:
		print(f.data)
	else:
		print("没有")
	return


if __name__ == '__main__':
	test()
