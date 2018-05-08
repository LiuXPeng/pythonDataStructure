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
	def __init__(self, data = None):
		self.data = data
		self.firstedge = None

class GraphAdjList(object):
	def __init__(self):
		self.nodeList = []
		self.numVertexes = 0
		self.numEdges = 0

	def createALGraph(self):
		self.numVertexes = int(input("请输入顶点数： "))
		self.numEdges = int(input("请输入边数： "))

		for x in range(self.numVertexes):
			self.nodeList.append(VertexNode(int(input("请输入顶点信息"))))

		for x in range(self.numEdges):
			i = int(input("请输入vi的i"))
			j = int(input("请输入vj的j"))
			e = edgeNode()
			e.adjvex = j
			e.next = self.nodeList[i].firstedge
			self.nodeList[i].firstedge = e
			e.adjvex = i
			e = edgeNode()
			e.adjvex = i
			e.next = self.nodeList[j].firstedge
			self.nodeList[j].firstedge = e

	def showGraph(self):
		for L in self.nodeList:
			pass
		return
#test
def test():
	sample = GraphAdjList()
	sample.createALGraph()
	sample.showMGraph()
	return

if __name__ == '__main__':
	test()

