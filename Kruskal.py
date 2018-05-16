#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Kruskal'

__author__ = 'lxp'

#《大话数据结构》251页，最小生成树Kruskal算法

class Edge(object):
	def __init__(self):
		self.begin = None
		self.end = None
		self.weight = None

def find(parent, f):
	while parent[f] > 0:
		f = parent[f]
	return f

def miniSpanTree_Kruskal():
	edges = []
	vex = int(input("请输入顶点数"))
	parent = [0] * vex
	edge_num = int(input("请输入边数"))
	edge = Edge()

	#创建252页的边表
	print("请输入边的下标i, j; 要求： i > j。")
	for i in range(edge_num):
		edge = Edge()
		edge.begin = int(input("请输入边的下标i: "))
		edge.end = int(input("请输入边的下标j: "))
		edge.weight = int(input("请输入边的权重： "))
		if len(edges) == 0 or edge.weight >= edges[-1].weight:
			edges.append(edge)
			continue
		for j in range(len(edges)):
			if edge.weight < edges[j].weight:
				edges.insert(j, edge)
				break

	#Kruska算法过程
	for i in range(edge_num):
		n = find(parent, edges[i].begin)
		m = find(parent, edges[i].end)
		if n != m:
			parent[n] = m
			print("本次循环选择边的节点和权重： " , edges[i].begin, ',', edges[i].end, ',', edges[i].weight)

	return


#test
def test():
	miniSpanTree_Kruskal()
	return

if __name__ == '__main__':
	test()