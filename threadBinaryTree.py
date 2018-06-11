#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'thread binary tree'

__author__ = 'lxp'

#《大话数据结构》191页

import binaryTree

class BiThrNode(object):
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None
		self.ltag = False
		self.rtag = False


class ThBiTree(object):
	def __init__(self):
		self.lchild = None
		self.rchild = None


#中序遍历进行中序线索化
def inThreading(p):
	global pre
	pre = None
	def method(p):
		global pre
		if p:
			method(p.lchild)
			if not p.lchild:
				p.ltag = True
				p.lchild = pre
			if pre and not pre.rchild:
			#在这里，书上192页伪代码并没有处理pre最开始是NULL的情况，但不处理要报错
				pre.rtag = True
				pre.rchild = p
			pre = p
			method(p.rchild)
	method(p.lchild)

def InOrderTraverse_Thr(T):
	p = T.lchild
	while p != T:
		while p.ltag == False:
			p = p.lchild
		print(p.data, ' ', end = '')
		while p.rtag == True and p.rchild != T:
			p = p.rchild
			print(p.data, ' ', end = '')
		p = p.rchild
	print('')#换行
	return

#二叉树转化为线索二叉树
def Bitree2Thbitree(BT):
	res = ThBiTree()
	if BT.head == None:
		res.head = None
		return res
	res.lchild = BiThrNode(BT.head.data)
	def method(BNode, TNode):
		if BNode.rchild != None:
			TNode.rchild = BiThrNode(BNode.rchild.data)
			method(BNode.rchild, TNode.rchild)
		if BNode.lchild != None:
			TNode.lchild = BiThrNode(BNode.lchild.data)
			method(BNode.lchild, TNode.lchild)
		return
	method(BT.head, res.lchild)
	inThreading(res)
	#res.preOrderTraverse_th()
	mark = res.lchild
	while mark.lchild != None:
		mark = mark.lchild
	mark.lchild = res
	while mark.rchild != None:
		mark = mark.rchild
	res.rchild = mark
	mark.rchild = res
	return res


#test
def test():
	S = ['A', 'B', '#', 'D', '#', '#', 'C', '#', '#']
	T = binaryTree.preOrderCreate(S)
	T.preOrderTraverse()
	U = Bitree2Thbitree(T)
	InOrderTraverse_Thr(U)
	A = binaryTree.BitNode('A')
	B = binaryTree.BitNode('B')
	C = binaryTree.BitNode('C')
	D = binaryTree.BitNode('D')
	E = binaryTree.BitNode('E')
	F = binaryTree.BitNode('F')
	G = binaryTree.BitNode('G')
	H = binaryTree.BitNode('H')
	I = binaryTree.BitNode('I')
	A.lchild = B
	A.rchild = C
	B.lchild = D
	C.lchild = E
	C.rchild = F
	D.lchild = G
	D.rchild = H
	E.rchild = I
	tree = binaryTree.BiTree()
	tree.head = A
	tree.preOrderTraverse()#前序遍历
	U = Bitree2Thbitree(tree)
	InOrderTraverse_Thr(U)#中序遍历，所以不一样

if __name__ == '__main__':
	test()