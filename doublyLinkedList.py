#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'doubly linked list'

__author__ = 'lxp'

#《大话数据结构》81页

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.pre = None

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.length = 0

	def showList(self):
		if self.head == Node:
			return
		pre = self.head
		while pre.next != self.head:
			print(pre.data)
			pre = pre.next
		print(pre.data)

	def add(self, data):
		node = Node(data)
		self.length = self.length + 1
		if self.head == None:
			self.head = node
			node.next = node
			node.pre = node
			return
		nex = self.head
		pre = nex.pre
		node.next = nex
		node.pre = pre
		pre.next = node
		nex.pre = node

	def getNode(self, index):
		if index < 0 or index > self.length - 1:
			return
		loc = self.head
		for i in range(index):
			loc = loc.next
		return loc.data

	def insert(self, data, index):
		if index < 0 or index > self.length:
			return
		node = Node(data) 
		loc = self.head
		if index == 0:
			self.head = node
		for i in range(index):
			loc = loc.next
		node.pre = loc.pre
		node.next = loc
		loc.pre.next = node
		loc.pre = node
		self.length = self.length + 1
		return

	def delete(self, index):
		if index < 0 or index > self.length - 1:
			return
		loc = self.head
		for i in range(index):
			loc = loc.next
		loc.pre.next = loc.next
		loc.next.pre = loc.pre
		return 


#test
def test():
	L = DoublyLinkedList()
	for i in range(10):
		L.add(i)
	L.insert(100, 0)
	print(L.getNode(2))
	L.delete(5)
	L.showList()

if __name__ == '__main__':
	test()