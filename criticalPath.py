#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' critical path of networked'

__author__ = 'lxp'

#《大话数据结构》281页

import linkStack

class EdgeNode(object):
	def __init__(self):
		self.adjvex = None
		self.weight = 1
		self.next = None

class VertexNode(object):
	def __init__(self, data = None):
		self.in_ = 0
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
			self.nodeList.append(VertexNode(input("请输入顶点信息")))

		for x in range(self.numEdges):
			i = int(input("请输入vi的i"))
			j = int(input("请输入vj的j"))
			weight = int(input("请输入权重"))
			e = EdgeNode()
			e.weight = weight
			e.adjvex = j
			e.next = self.nodeList[i].firstedge
			self.nodeList[i].firstedge = e
			self.nodeList[j].in_ = self.nodeList[j].in_ + 1

	def showGraph(self):
		for L in self.nodeList:
			print(L.data, ', 入度：', L.in_, ', ', end = '')
			index = L.firstedge
			while index != None:
				print(index.adjvex, ' ', end = '')
				index = index.next
			print('\n')
		return

def topologicalSort(GL):
	count = 0
	stack = linkStack.LinkStack()
	top = 0
	for i in range(GL.numVertexes):
		if GL.nodeList[i].in_ == 0:
			stack.push(i)
			top = top + 1
	top2 = 0
	stv = [0] * GL.numVertexes
	stack2 = linkStack.LinkStack()
	while top != 0:
		gettop = stack.pop()
		top = top - 1
		count = count + 1
		stack2.push(gettop)
		top2 = top2 + 1
		e = GL.nodeList[gettop].firstedge
		while e:
			k = e.adjvex
			GL.nodeList[k].in_ = GL.nodeList[k].in_ - 1
			if GL.nodeList[k].in_ == 0:
				stack.push(k)
				top = top + 1
			if etc[gettop] + e.weight > etv[k]:
				etv[k] = etv[gettop] + e.weight
			e = e.next

	if count < GL.numVertexes:
		print("图中有环")
	return etv, stack2, top2

def criticalPath(GL):
	etv, stack2, top2 = topologicalSort(GL)
	ltv = []
	for i in GL.numVertexes:
		ltv.append(etv[GL.numVertexes - 1])
	while top2 != 0:
		gettop = stack2.pop()
		top2 = top2 - 1
		e = GL.nodeList[gettop].firstedge
		while e:
			k = e.adjvex
			if ltv[k] - e.weight < ltv[gettop]:
				ltv[gettop] = ltv[k] - e.weight
			e = e.next
	for j in range(GL.numVertexes):
		e = GL.nodeList[j].firstedge
		while e:
			k = e.adjvex
			ete = etv[j]
			lte = ltv[k] - e.weight
			if ete == lte:
				print(GL.nodeList[j].data, GL.nodeList[k].data, e.weight)
			e = e.next
	return


#test
def test():
	sample = GraphAdjList()
	sample.createALGraph()
	sample.showGraph()
	criticalPath(sample)
	return
	return

if __name__ == '__main__':
	test()
