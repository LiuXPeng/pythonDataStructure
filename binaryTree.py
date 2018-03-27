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