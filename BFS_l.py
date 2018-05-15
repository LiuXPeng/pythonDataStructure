#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'breadth first search'

__author__ = 'lxp'

#《大话数据结构》244页，基于邻接表的广度优先遍历

import linkQueue
import adjacencyList

def BFSTraverse(GL):
	Q = linkQueue.LinkQueue()
	visited = [False] * GL.numVertexes
	for i in range(GL.numVertexes):
		if not visited[i]:
			visited[i] = True
			print(GL.nodeList[i].data)
			Q.enQue(i)
			while not Q.quenueEmpty():
				i = Q.deQue()
				p = GL.nodeList[i].firstedge
				while p:
					if not visited[p.adjvex]:
						visited[p.adjvex] = True
						print(GL.nodeList[p.adjvex].data)
						Q.enQue(p.adjvex)
					p = p.next

#test
def test():
	sample = adjacencyList.GraphAdjList()
	sample.createALGraph()
	sample.showGraph()
	BFSTraverse(sample)
	return

if __name__ == '__main__':
	test()