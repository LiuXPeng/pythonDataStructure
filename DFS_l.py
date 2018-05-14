#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'depth first search'

__author__ = 'lxp'

#《大话数据结构》241页，基于邻接表的深度优先遍历

import adjacencyList

def DFS(GL, i):
	global visited
	visited[i] = True
	print(GL.nodeList[i].data)
	p = GL.nodeList[i].firstedge
	while p:
		if not visited[p.adjvex]:
			DFS(GL, p.adjvex)
		p = p.next

def DFSTraverse(GL):
	global visited
	visited = [False] * GL.numVertexes
	for i in range(GL.numVertexes):
		if not visited[i]:
			DFS(GL, i)
	return


#test
def test():
	sample = adjacencyList.GraphAdjList()
	sample.createALGraph()
	sample.showGraph()
	DFSTraverse(sample)
	return

if __name__ == '__main__':
	test()