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

def r_Rotate(p):
	L = BiTNode()
	L = p.lchild
	p.lchild = L.rchild
	L.rchild = p
	return L

def l_Rotate(p):
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
		elif L.bf == 0:
			pass
		else:
			L.bf = 1
		Lr.bf = 0
		T.lchild = l_Rotate(T.lchild)
		T = r_Rotate(T)
	return T

def rightBalance(T):
	R = T.rchild
	if R.bf == -1:
		T.bf = R.bf = 0
		T = l_Rotate(T)
	if R.bf == 1:
		Rl = R.lchild
		if Rl.bf == -1:
			R.bf = 0
		elif Rl.bf == 0:
			pass
		else:
			R.bf == -1
		Rl.bf = 0
		T.rchild = r_Rotate(T.rchild)
		T = l_Rotate(T)
	return T

def insertAVL(T, e, taller, mark):
	if not T:
		T = BiTNode()
		T.data = e
		T.bf = 0
		taller = True


	else:
		if e == T.data:
			taller = False
			return T, e, taller, False

		if e < T.data:
			T.lchild, e, taller, mark = insertAVL(T.lchild, e, taller, mark)
			if not mark:
				return T, e, taller, False
			if taller:
				if T.bf == 1:
					T = leftBalance(T)
					taller = False
				elif T.bf == 0:
					T.bf = 1
					taller = True
				else:
					T.bf = 0
					taller = False

		else:
			T.rchild, e, taller, mark = insertAVL(T.rchild, e, taller, mark)
			if not mark:
				return T, e, taller, False
			if taller:
				if T.bf == 1:
					T.bf = 0
					taller = False
				elif T.bf == 0:
					T.bf = -1
					taller = True
				else:
					T = rightBalance(T)
					taller = False

	return T, e, taller, True

def showTree(T):
	if not T:
		print("树为空树")
		return
	L = [T]
	while len(L) != 0:
		print(L[0].data, ',', end = '')
		if L[0].lchild:
			L.append(L[0].lchild)
		if L[0].rchild:
			L.append(L[0].rchild)
		del L[0]
	print()
	return


			
#test
def test():
	L = [3, 2, 1, 4, 5, 6, 7, 10, 9, 8]
	T = None
	for i in L:
		T, e, taller, mark = insertAVL(T, i, False, False)
		showTree(T)
	#showTree(T)
	return

if __name__ == '__main__':
	test()
