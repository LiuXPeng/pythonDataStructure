#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'adjacency matrix'

__author__ = 'lxp'

#《大话数据结构》227页

import numpy as np

class MGraph():
	def __init__(self):
		self.vexs = []
		self.arc = None
		self.numVertexes = a
		self.numEdges = 0

	def createMGraph(self):
		self.numVertexes, self.numEdges = input("请输入点数和边数")
		self.arc = np.zeros([self.numVertexes, self.numVertexes])
		for x in range(self.numEdges):
			vi, vj, w = input("请输入边（vi, vj）的下标i、j以及权重w")
			self.arc[i][j] = self.arc[j][i] = w
		return

	def showMGraph(self):
		print(self.MGraph)
		return

#test
def test():
	pass

if __name__ == '__main__':
	test()


