#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'sequence stack'

__author__ = 'lxp'

#《大话数据结构》92页

class SeqStack(object):
	def __init__(self, maxSize = 30):
		self.top = -1
		self.maxSize = maxSize
		self.data = [None] * maxSize

	def push(self, data):
		if self.top > self.maxSize - 1:
			return
		self.top = self.top + 1
		self.data[self.top] = data
		return

	def pop(self):
		if self.top == -1:
			return
		self.top = self.top - 1
		return self.data[self.top + 1]

	def showStack(self):
		#if top == -1:
		#	return
		for x in range(self.top):
			print(self.data[x], ',',end = '')
		print('')
		return


#test
def test():
	L = SeqStack(100)
	for x in range(10):
		L.push(x)
		if x % 3 == 0:
			print(L.pop())
	L.showStack()

if __name__ == '__main__':
	test()