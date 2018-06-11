#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'circle queue'

__author__ = 'lxp'

#《大话数据结构》80页

class CirQueue(object):
	def __init__(self, maxSize = 30):
		self.rear = 0
		self.front = 0
		self.maxSize = maxSize
		self.data = [None] * self.maxSize

	def isEmpty(self):
		return self.rear == self.front

	def isFull(self):
		return (self.rear - self.front + 1) % self.maxSize == 0

	def getLength(self):
		return (self.rear - self.front + self.maxSize) % self.maxSize

	def enQue(self, data):
		if self.isFull():
			return
		self.data[self.rear] = data
		self.rear = (self.rear + 1) % self.maxSize

	def deQue(self):
		if self.isEmpty():
			return
		res = self.data[self.front]
		self.front = (self.front + 1) % self.maxSize
		return res

	def showQue(self):
		for x in range(self.getLength()):
			index = (x + self.front) % self.maxSize 
			print(self.data[index],' ',end = '')
		return


#test
def test():
	L = CirQueue(15)

	for x in range(10):
		L.enQue(x)
	L.showQue()
	print(' ')

	for x in range(3):
		print(L.deQue())
	L.showQue()
	print(' ')

	for x in range(10):
		L.enQue(x + 10)
	L.showQue()
	print(' ')

if __name__ == '__main__':
	test()