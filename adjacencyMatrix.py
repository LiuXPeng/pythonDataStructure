#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'adjacency matrix'

__author__ = 'lxp'

#《大话数据结构》227页
#在后面图的遍历会调用这个模块，在review时候发现。
#后面的遍历针对的是无权无向图，在那两个模块中，判断联通的条件是权值为1
#因为后两个模块要求的权值输入，若联通则权值输1

import numpy as np

class MGraph(object):
	def __init__(self):
		self.vexs = []
		self.arc = None
		self.numVertexes = 0
		self.numEdges = 0

	def createMGraph(self):
		self.numVertexes = int(input("请输入点数: "))
		self.numEdges = int(input("请输入边数: "))
		self.arc = np.zeros([self.numVertexes, self.numVertexes])

		for x in range(self.numVertexes):
			self.vexs.append(input("依次输入顶点信息: "))

		for i in range(self.numVertexes):
			for j in range(self.numVertexes):
				if i != j:
					self.arc[i][j] = float("inf")

		for x in range(self.numEdges):
			vi = int(input("请输入边（vi, vj）的下标i: "))
			vj = int(input("请输入边（vi, vj）的下标j: "))
			w = int(input("请输入边（vi, vj）的权重w: "))
			self.arc[vi][vj] = self.arc[vj][vi] = w
			
		return

	def showMGraph(self):
		print(self.arc)
		return

#test
def test():
	sample = MGraph()
	sample.createMGraph()
	sample.showMGraph()
	return

if __name__ == '__main__':
	test()

###input输入的是str，需要转换
