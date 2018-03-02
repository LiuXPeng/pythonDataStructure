#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'sequence list'

__author__ = 'lxp'

class Seqlist(object):
	def __init__(self, maxsize = 30):
		self.maxsize = maxsize
		self.data = [None] * maxsize
		self.length = 0

	def showlist(self):
		for i in range(self.length):
			print(self.data[i])

	def add(self, data):
		if self.length == self.maxsize:
			return
		self.data[i] = data
		self.length = self.length + 1

	def insert(self, data, index):
		if self.length == self.maxsize - 1 or index > self.length:
			return
		for i in range(self.length - index):
			self.data[self.length - i] = self.data[self.length - i - 1] 
		self.data[index] = data
		self.length = self.length + 1

	def getNode(self, index):
		if index > self.length - 1 or index < 0:
			return
		return self.data[index]

	def delete(self, index):
		if index > self.length - 1 or index < 0:
			return
		for i in range(self.length - index - 1):
			self.data[index + i] = self.data[index + i + 1]
		self.length = self.length - 1


#test
L = Seqlist(10)
for i in range(8):
	L.add(i)
L.insert(100, 0)
L.delete(100)
L.showlist()

print(L.getNode(10))