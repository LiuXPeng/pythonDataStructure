#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'depth first search'

__author__ = 'lxp'

#《大话数据结构》240页

import adjacencyMatrix

def DFS(G, i):
	global visited
	visited[i] = True
	print(G.vexs[i])
	for j in range(G.numVertexes):
		if G.arc[i][j] == 1 and not visited[j]:
			DFS(G, j)

def DFSTraverse(G):
	global visited
	visited = [False] * G.numVertexes
	for i in range(G.numVertexes):
		if not visited[i]:
			DFS(G, i)
		


#test
def test():
	sample = adjacencyMatrix.MGraph()
	sample.createMGraph()
	sample.showMGraph()
	DFSTraverse(sample)
	return

if __name__ == '__main__':
	test()