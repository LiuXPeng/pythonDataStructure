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
		self.head = None

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