#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'double stack'

__author__ = 'lxp'

class DoubStack(object):
	def __init__(self, maxSize = 30):
		self.top0 = 0
		self.top1 = 0
		self.maxSize = maxSize
		self.data = [None] * maxSize

	def push(self, data, stackName = 0):
		if self.top1 + self.top0 == self.maxSize:
			return

		if stackName == 0:
			self.data[self.top0] = data
			self.top0 = self.top0 + 1
			return

		self.data[self.maxSize - self.top1 -1] = data
		self.top1 = self.top1 + 1
		return

	def pop(self, stackName = 0):
		if stackName == 0:
			if self.top0 == 0:
				return
			self.top0 = self.top0 - 1
			return  self.data[self.top0]

		if self.top1 == 0:
			return
		self.top1 = self.top1 - 1
		return self.data[self.maxSize - self.top1 - 1]

	def showStack(self):
		for x in range(self.top0):
			print(self.data[x], ' ', end = '')
		print(' ')
		for x in range(self.top1):
			print(self.data[self.maxSize - x - 1],' ', end = '')
		return



#test
#test
L = DoubStack()
for x in range(10):
	L.push(x)
	if x % 3 == 0:
		print(L.pop())

for x in range(10):
	L.push(100 - x, 1)
	if x % 3 == 0:
		print(L.pop(1))


L.showStack()

		