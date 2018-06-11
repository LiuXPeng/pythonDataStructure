#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'linked list'

#《大话数据结构》59页

__author__ = 'lxp'

class LinkNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkList(object):
	def __init__(self):
		self.head = None
		self.length = 0

	def isEmpty(self):
		return self.head is None

	def printList(self):
		pre = self.head
		'''
		if pre = None:
			return None
		'''
		while pre != None:
			print(pre.data)
			pre = pre.next

	def add(self, item):
		if self.isEmpty():
			self.head = LinkNode(item)
		else:
			pre = self.head
			while pre.next:
				pre = pre.next
			pre.next = LinkNode(item)
			self.length = self.length + 1

	def getNode(self, index):
		if index > self.length - 1 or index < 0:
			return None
		loc = self.head
		for x in range(index):
			loc = loc.next
		return loc.data

	def insert(self, data, index):
		node = LinkNode(data)

		#0位置要特殊处理一下
		if index == 0:
			node.next = self.head
			self.head = node
			return 
		pre = self.head

		#find insert location
		for i in range(index - 1):
			pre = pre.next
			if pre == None:
				return None
		
		node.next = pre.next
		pre.next = node

	def delete(self, index):
		if index > self.length - 1 or index < 0:
			return 
		if index == 0:
			self.head = self.head.next
			return
		pre = self.head
		for i in range(index - 1):
			pre = pre.next
		pre.next = pre.next.next
			
				
#test
def test():
	L = LinkList()
	for i in range(10):
		L.add(i)
	#L.insert(11, 11)
	print(L.getNode(2))
	L.delete(10)
	L.printList()

if __name__ == '__main__':
	test()
