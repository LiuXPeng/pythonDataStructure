#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Floyd'

__author__ = 'lxp'

#《大话数据结构》247页，基于邻接矩阵的最短路径Floyd算法

import numpy as np
import adjacencyMatrix

def shortestPath_Floyd(G):
	D = np.zeros([G.numVertexes, G.numVertexes])
	P = np.zeros([G.numVertexes, G.numVertexes])
	for v in range(G.numVertexes):
		for w in range(G.numVertexes):
			D[w][v] = G.arc[w][v]
			P[v][w] = w

	for k in range(G.numVertexes):
		for v in range(G.numVertexes):
			for w in range(G.numVertexes):
				if D[v][w] > D[v][k] + D[k][w]:
					D[v][w] = D[v][k] + D[k][w]
					P[v][w] = P[v][k]

	for v in range(G.numVertexes):
		for w in range(v + 1, G.numVertexes):
			print(v, 'to', w, ', weight:', D[v][w], end = '')
			k = P[v][w]
			print(', path:', v, '', end = '')
			while k != w:
				k = int(k)
				print('->', k, end = '')
				k = P[k][w]
			print('->', w)


	return D, P


#test
def test():
	sample = adjacencyMatrix.MGraph()
	sample.createMGraph()
	sample.showMGraph()
	D, P = shortestPath_Floyd(sample)
	print('D:')
	print(D)
	print('P:')
	print(P)
	return

if __name__ == '__main__':
	test()