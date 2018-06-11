#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'sequence string'

__author__ = 'lxp'

#实现《大话数据结构》128页“串”结构，书中每个函数绝大部分有函数说明

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
			print(self.data[x + 1],',',end = '')
		print('')

def isSeqStr(S):
	return isinstance(S, SeqString)

#把T复制给S
def strCopy(T, S):
	if not isSeqStr(S) or not isSeqStr(T):
		return
	S.length = min(S.data[0], T.length)
	for x in range(S.length):
		S.data[x + 1] = T.data[x + 1]
	return

#生成一个其值等于字符串的串
def strAssign(data):
	return SeqString(len(data), data)

def strCompare(T, S):
	if not isSeqStr(S) or not isSeqStr(T):
		return
	for x in range(min(T.length, S.length)):
		if T.data[x + 1] > S.data[x + 1]:
			return 1
		if T.data[x + 1] < S.data[x + 1]:
			return -1
	if T.length > S.length:
		return 1
	elif T.length == S.length:
		return 0
	else:
		return -1

#连接S1， S2
def concat(S1, S2):
	T = SeqString(S1.length + S2.length)
	for x in range(S1.length):
		T.add(S1.data[x + 1])
	for x in range(S2.length):
		T.add(S2.data[x + 1])
	return T

def subStr(S, pos, length):
	if not isSeqStr(S) or pos < 1 or pos > S.strLen() or length < 0 or length + pos - 1 > S.strLen():
		return
	sub = SeqString(length)
	for i in range(length):
		sub.add(S.data[pos + i])
	return sub

#查找主串S中字串T在pos之后出现的位置
def index(S, T, pos = 1):
	if not isSeqStr(S) or not isSeqStr(T) or pos > S.length - T.length + 1:
		return
	if S.length < T.length:
		return
	for x in range(S.length - T.length + 1):
		if x + 1 < pos:
			continue
		for i in range(T.length):
			if (S.data[x + i + 1] != T.data[i + 1]):
				break
			if i == T.length - 1:
				return x + 1
	return

def replace(S, T, V):
	pos = index(S, T)
	while pos != None:
		if S.length - T.length + V.length > S.data[0]:
			return
		strDelete(S, pos, T.length)
		strInsert(S, pos, V)
		pos = pos + V.length
		pos = index(S, T, pos)
	return

def strInsert(S, pos, T):
	if not isSeqStr(S) or not isSeqStr(T) or S.length + T.length > S.data[0] or pos < 1 or pos > S.length:
		return
	for x in range(T.length):
		S.add(T.data[x + 1], pos + x)
	return

def strDelete(S, pos, length):
	if not isSeqStr(S) or pos < 1:
		return
	if pos + length > S.length + 1:
		return
	for x in range(length):
		S.delete(pos)
	return
	

#test
def test():
	L = SeqString(100, data = 'abcdefgabcdefgabcdefgabcdefg')
	L.showStr()

	L.add('e',5)
	L.showStr()

	L.delete(3)
	L.showStr()

	L.delete(3)
	L.showStr()

	print(L.isStrEmpty())
	print(L.strLen())

	print(isSeqStr(1))
	print(isSeqStr(L))

	print('copy')
	S = SeqString(7)
	strCopy(L, S)
	S.showStr()

	A = strAssign('abc')
	A.showStr()

	print(strCompare(A, L))

	A.showStr()
	L.showStr()

	B = concat(A, L)
	B.showStr()


	C = subStr(B, 1, 2)
	C.showStr()



	print(index(B, C, 2))

	strInsert(L, 4, C)

	L.showStr()

	L.showStr()
	print('L')
	S.showStr()
	print('S')
	A.showStr()
	print('A')
	B.showStr()
	print('B')
	C.showStr()
	print('C')
	print('=============')
	D = SeqString(data = 'XXXXXX')
	L.showStr()
	print('L')
	replace(L, A, D)
	L.showStr()
	print('L')

if __name__ == '__main__':
	test()