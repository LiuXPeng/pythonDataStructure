#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'thread binary tree'

__author__ = 'lxp'

#《大话数据结构》191页

class BiThrNode(object):
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None
		self.ltag = None
		self.rtag = None

class ThBiTree(object):
	def __init__(self):
		self.head = None

#中序遍历进行中序线索化
	def inThreading(BT):
