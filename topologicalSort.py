#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'topological ordering'

__author__ = 'lxp'

#《大话数据结构》273页

import linkStack

class EdgeNode(object):
	def __init__(self):
		self.adjvex = None
		self.weight = 1
		self.next = None

class VertexNode(object):
	def __init__(self):
		self.in_ = 0
		self.data = None
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
			self.nodeList.append(VertexNode(input("请输入顶点信息")))

		for x in range(self.numEdges):
			i = int(input("请输入vi的i"))
			j = int(input("请输入vj的j"))
			e = EdgeNode()
			e.adjvex = j
			e.next = self.nodeList[i].firstedge
			self.nodeList[i].firstedge = e
			e = EdgeNode()
			e.adjvex = i
			e.next = self.nodeList[j].firstedge
			self.nodeList[j].firstedge = e
			self.nodeList[j].in_ = self.nodeList[j].in_ + 1

def topologicalSort(GL):
	top = 0
	count = 0
	stack = linkStack.LinkStack()
	for i in range(GL.numVertexes):
		if GL.nodeList[i].in_ == 0:
			stack.push(i)
			top = top + 1
	while top != 0:
		gettop = stack.pop()
		top = top - 1
		print(GL.nodeList[gettop].data)
		count = count + 1
		e = GL.nodeList[gettop].firstedge
		while e:
			k = e.adjvex
			if not GL.nodeList[k].in_:
				stack.puss(k)
				top = top + 1
			e = e.next

		if count < GL.numVertexes:
			print("图中有环")
			return
	return


#test
def test():
	sample = GraphAdjList()
	topologicalSort(sample)
	return

if __name__ == '__main__':
	test()