#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Prim'

__author__ = 'lxp'

#《大话数据结构》247页，基于邻接矩阵的最小生成树Prim算法

import adjacencyMatrix

def miniSpanTree_Prim(G):
	lowcost = []
	adjvex = []
	for i in range(G.numVertexes):
		lowcost.append(G.arc[0][i])
		adjvex.append(0)
	for i in range(1, G.numVertexes):
		min_ = float('inf')
		j = 1
		k = 0
		while j < G.numVertexes:
			if lowcost[j] != 0 and lowcost[j] < min_:
				min_ = lowcost[j]
				k = j
			j = j + 1
		print("本次循环选择边的下标为： ", adjvex[k], k)
		for j in range(1, G.numVertexes):
			if G.arc[k][j] < lowcost[j]:
				lowcost[j] = G.arc[k][j]
				adjvex[j] = k

	return


#test
def test():
	sample = adjacencyMatrix.MGraph()
	sample.createMGraph()
	sample.showMGraph()
	miniSpanTree_Prim(sample)
	return

if __name__ == '__main__':
	test()