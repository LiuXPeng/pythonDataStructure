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
		self.numVertexes = 0
		self.numEdges = 0

	def createMGraph(self):
		self.numVertexes = int(input("请输入点数"))
		self.numEdges = int(input("请输入边数"))
		self.arc = np.zeros([self.numVertexes, self.numVertexes])
		for x in range(self.numEdges):
			vi = int(input("请输入边（vi, vj）的下标i"))
			vj = int(input("请输入边（vi, vj）的下标j"))
			w = int(input("请输入边（vi, vj）的权重w"))
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


