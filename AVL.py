#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Self-balancing binary search tree'

__author__ = 'lxp'

#《大话数据结构》335页

class BiTNode(object):
	def __init__(self):
		self.data = None
		self.bf = 0
		self.lchild = None
		self.rchild = None

def r_Rotate(P):
	L = BiTNode()
	L = p.lchild
	p.lchild = L.rchild
	L.rchild = p
	return L

def l_Rotate(P):
	R = BiTNode()
	R = p.rchild
	p.rchild = R.lchild
	R.lchild = p
	return R

def leftBalance(T):
	L = T.lchild
	if L.bf == 1:
		T.bf = L.bf = 0
		T = r_Rotate(T)
	elif L.bf == 0:
		Lr = L.rchild
		if Lr.bf == 1:
			L.bf = 0
			break
		elif L.bf == 0:
			break
		else:
			L.bf = 1
		Lr.bf = 0
		T.lchild = l_Rotate(T.lchild)
		T = r_Rotate(T)
	return T

def rightBalance(T):
	R = T.rchild
	if R.bf == -1:
		T.bf = r.bf = 0
		T = l_Rotate(T)
	if R.bf == 1:
		Rl = R.lchild
		if Rl.bf == -1:
			R.bf = 0
		elif Rl.bf == 0:
			break
		else:
			R.bf == -1
			break
		Rl.bf = 0
		T.rchild = r_Rotate(T.rchild)
		T = l_Rotate(T)
	return T

def insertAVL(T, e):
	if T:
		pass
	else:
		T = BiTNode()
		T.data = e
	return T

#test
def test():
	pass
	return

if __name__ == '__main__':
	test()