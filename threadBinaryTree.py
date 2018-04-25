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
	pre = None
	def method(p):
		if p:
			global pre
			method(p.lchild)
			if not p.lchild:
				p.ltag = True
				p.lchild = pre
			if not pre.rchild:
				pre.rtag = True
				pre.rchild = p
			pre = p
			method(p.rchild)
		return

def InOrderTraverse_Thr(T):
	p = T.lchild
	while p ! = T:
		while p.ltag == False:
			p = p.lchild
		print(P.data, ' ', end = '')
		while p.rtag == True:
			p = p.rchild
			print(p.data, ' ', end = '')
		p = p.rchild
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
	method(BT.head, res.head)
	inThreading(res)
	mark = res.lchild
	while mark.lchild != None:
		mark = mark.lchild
	mark.lchild = lchild
	while mark.rchild != None:
		mark = mark.rchild
	res.rchild = mark
	mark.rchild = res
	return res