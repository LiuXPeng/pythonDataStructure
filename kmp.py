#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'kmp algorithm'

__author__ = 'lxp'

#基本结构参考sequence string
class SeqString(object):
	def __init__(self, maxSize = 30, data = ""):##
		self.data = [None] * (maxSize + 1)
		self.data[0] = max(maxSize, len(data))
		self.length = 0
		for x in data:
			self.length = self.length + 1
			self.data[self.length] = x
			if self.length == maxSize:
				break
		return

	def add(self, data, index = None):
		#给第index前面插入
		if self.length == self.data[0]:
			return		
		if index == None:
			self.length = self.length + 1
			self.data[self.length] = data
			return
		if index > self.length + 1:
			return
		self.length = self.length + 1
		for i in range(self.length - index):
		#self.length已经++
			self.data[self.length - i] = self.data[self.length - i - 1]
		self.data[index] = data
		return

	def delete(self, index):
		if index < 1 or index > self.length:
			return
		for x in range(self.length - index):
			self.data[index + x] = self.data[index + x + 1]
		self.length = self.length - 1
		return

	def cleanStr(self):
		self.length = 0
		return

	def isStrEmpty(self):
		return self.length == 0

	def strLen(self):
		return self.length

	def showStr(self):
		for x in range(self.length):
			print(self.data[x + 1],' ',end = '')

#生成一个其值等于字符串的串
def strAssign(data):
	return SeqString(len(data), data)

'''
#这里很精髓，注意else后面j的回溯：发现不同以后，立刻回溯到一个地方，
#这个地方使j前面的和i前面对应的又相等,继续比较下一个
#《大话数据结构》141页
'''
def getNext(T):
	res = [0]
	i, j = 1, j = 0
	while i < T.length:
		if j == 0 or T.data[i] == T.data[j]:
			i = i + 1
			j = j + 1
			res.append(j)
		else:
			j = res[j]