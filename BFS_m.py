#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'breadth first search'

__author__ = 'lxp'

#《大话数据结构》243页，基于邻接矩阵的广度优先遍历

import adjacencyMatrix
import linkQueue

def BFSTraverse(G):
	Q = linkQueue.LinkQueue()
	visited = [False] * G.numVertexes
	for i in range(G.numVertexes):
		if not visited[i]:
			visited[i] = True
			print(G.vexs[i])
			Q.enQue(i)
			while not Q.quenueEmpty():
				i = Q.deQue()
				for j in range(G.numVertexes):
					if G.arc[i][j] == 1 and not visited[j]:
						visited[j] = True
						print(G.vexs[j])
						Q.enQue(j)


#test
def test():
	sample = adjacencyMatrix.MGraph()
	sample.createMGraph()
	sample.showMGraph()
	BFSTraverse(sample)
	return

if __name__ == '__main__':
	test()