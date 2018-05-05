#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Adjacency List'

__author__ = 'lxp'

#《大话数据结构》231页

class EdgeNode(object):
	def __init__(self):
		self.adjvex = None
		self.weight = None
		self.next = None

class VertexNode(object):
	def __init__(self):
		self.data = None
		self.edgeNode = None

class GraphAdjList(object):
	def __init__(self):
		self.nodeList = []
		self.numVertexes = 0
		self.numEdges = 0

	def createALGraph(self):
		self.numVertexes = int(input("请输入顶点数： "))
		self.numEdges = int(input("请输入边数： "))

		for x in range(self.numVertexes):
			self.nodeList.append()	

