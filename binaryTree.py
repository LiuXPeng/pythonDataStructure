#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'binary tree'

__author__ = 'lxp'

class BitNode(object):
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None

class BiTree(object):
	def __init__(self):
		self.head = None

#前序遍历
	def preOrderTraverse(self):
		def method(T):
			if T == None:
				return
			print(T.data, ',', end = '')
			method(T.lchild)
			method(T.rchild)

		method(self.head)
		print()

#中序遍历
	def inOrderTraverse(self):
		def method(T):
			if T == None:
				return
			method(T.lchild)
			print(T.data, ',', end = '')
			method(T.rchild)

		method(self.head)
		print()


#后序遍历
	def postOrderTraverse(self):
		def method(T):
			if T == None:
				return
			method(T.lchild)
			method(T.rchild)
			print(T.data, ',', end = '')

		method(self.head)
		print()

#层序遍历
	def levelOrderTraverse(self):
		def method(L):
			while len(L) != 0 and L[0] == None:#这样某个子树为空，可以跳过
				del L[0]
			if len(L) == 0:
				return
			print(L[0].data, ',', end = '')
			L.append(L[0].lchild)
			L.append(L[0].rchild)
			del L[0]
			method(L)

		L = []
		L.append(self.head)
		method(L)
		print()

#test
A = BitNode('A')
B = BitNode('B')
C = BitNode('C')
D = BitNode('D')
E = BitNode('E')
F = BitNode('F')
G = BitNode('G')
H = BitNode('H')
I = BitNode('I')
A.lchild = B
A.rchild = C
B.lchild = D
C.lchild = E
C.rchild = F
D.lchild = G
D.rchild = H
E.rchild = I
tree = BiTree()
tree.head = A
tree.preOrderTraverse()
tree.inOrderTraverse()
tree.postOrderTraverse()
tree.levelOrderTraverse()