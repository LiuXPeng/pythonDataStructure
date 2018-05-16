#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Dijkstra'

__author__ = 'lxp'

#《大话数据结构》260页，基于邻接矩阵的最短路径Dijkstra算法

import adjacencyMatrix

def shortestPath_Dijkstra(G, v0):
	final = [0] * G.numVertexes
	P = [0] * G.numVertexes
	D = []
	for i in range(G.numVertexes):
		D.append(G.arc[v0][i])
	D[v0] = 1
	for v in range(1, G.numVertexes):
		min_ = float('inf')
		for w in range(G.numVertexes):
			if not final[w] and D[w] < min_:
				k = w
				min_ = D[w]
		final[k] = 1
		for w in range(G.numVertexes):
			if not final[w] and (min_ + G.arc[k][w]) < D[w]:
				D[w] = min_ + G.arc[k][w]
				P[w] = k

	return P		

#test
def test():
	sample = adjacencyMatrix.MGraph()
	sample.createMGraph()
	sample.showMGraph()
	res = shortestPath_Dijkstra(sample, 0)
	print(res)
	return

if __name__ == '__main__':
	test()