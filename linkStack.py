#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'link stack'

__author__ = 'lxp'

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkStack(object):
	def __init__(self):
		self.top = None
		self.length = 0

	def push(self, data):
		node = Node(data)
		self.length = self.length + 1
		if self.length == 1:
			self.top = node
			return
		node.next = self.top
		self.top = node
		return

	def pop(self):
		if self.length < 1:
			return
		self.length = self.length - 1
		res = self.top.data
		self.top = self.top.next
		return res

	def showStack(self):
		for x in range(self.length):
			print(self.top.data)
			self.top = self.top.next


#test
def test():
	L = LinkStack()
	for x in range(10):
		L.push(x)
		if x % 3 == 0:
			print(L.pop())
	L.showStack()
	return

if __name__ == '__main__':
	test()