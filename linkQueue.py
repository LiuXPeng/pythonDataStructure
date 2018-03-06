#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'link queue'

__author__ = 'lxp'

class Node(object):
	def __init__(self, data):
		self.next = None
		self.data = data

class LinkQueue(object):
	def __init__(self):
		node = Node(None)
		self.front = node
		self.rear = node

	def enQue(self, data):
		node = Node(data)
		self.rear.next = node
		self.rear = node
		return

	def deQue(self):
		if self.front.next == None:
			return
		res = self.front.next.data
		self.front = self.front.next
		return res

	def showQue(self):
		loc = self.front.next
		while loc != None:
			print(loc.data, ' ',end = '')
			loc = loc.next
		return


#test
L = LinkQueue()

for x in range(10):
	L.enQue(x)
L.showQue()
print(' ')

for x in range(8):
	print(L.deQue())
L.showQue()
print(' ')

for x in range(10):
	L.enQue(x + 10)
L.showQue()
print(' ')