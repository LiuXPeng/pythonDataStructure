#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'sequence string'

__author__ = 'lxp'

#实现《大话数据结构》128页“串”结构，书中每个函数绝大部分有函数说明

class SeqString(object):
	def __init__(self, maxSize, data = ""):
		self.data = [None] * (maxSize + 1)
		self.data[0] = maxSize
		self.length = 0
		for x in data:
			self.length = self.length + 1
			self.data[self.length] = x
			if self.length == maxSize:
				break
		return

	def add(self, data, index = None):
		#给第index前面插入
		if self.length == self.maxSize:
			return
		self.length = self.length + 1
		if index == None:
			self.data[self.length] = data
			return
		for i in range(self.length - index):
		#self.length已经++
			self.data[self.length - i] = self.data[self.length - i - 1]
		self.data[index] = data
		return

	def delete(self, index):
		if index < 1 or index > self.length:
			return
		for x in range(self.length - index):
			self.data[self.length - index + x] = self.data[self.length - index + x + 1]
		self.length = self.length - 1
		return

	def cleanStr(self):
		self.length = 0
		return

	def isStrEmpty(self):
		return self.length == 0

	def strLen(self):
		return self.length

def isSeqStr(S):
	return isinstance(S, SeqString)

def strCopy(T, S):
	if !isSeqStr(S) or !isSeqStr(T):
		return
	S.length = min(S.maxSize, T.length)
	for x in S.length:
		S.data[x + 1] = T.data[x + 1]
	return

def strAssign(data):
	return T = SeqString(data, len(data))

def strCompare(T, S):
	if !isSeqStr(S) or !isSeqStr(T):
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

def concat(S1, S2):
	T = SeqString(S1.length + S2.length)
	for x in range(S1.length):
		T.data[x + 1] = S1.data[x + 1]
	for x in range(S2.length):
		T.data[S1.length + x + 1] = S1.data[x + 1]
	return T

def subStr(S, pos, length):
	if !isSeqStr(S) or pos < 1 or pos > S.strLen() or length < 0 or length + pos - 1 > S.strLen():
		return
	sub = SeqString(length)
	for i in range(length):
		length.data[i + 1] = S.data[pos + i]
	return sub

def index(S, T, pos = 1):
	if !isSeqStr(S) or !isSeqStr(T) or pos > S.length - T.length:
		return
	if S.length < T.length:
		return
	for x in range(S.length - T.length):
		if x < pos - 1:
			break
		for i in range(T.length):
			if (S.data[x + i + 1] != T.data[i + 1]):
				break
			if i == T.length - 1:
				return x
	return

def replace(S, T, V):
	pos = index(S, T)
	while pos != None:
		if S.length - T.length + V.length > S.maxSize:
			return
		for x in range(T.length):
			S.delete(pos)
		strInsert(S, pos, T)
		pos = pos + T.length
		pos = index(S, T, pos)
	return

def strInsert(S, pos, T):
	if !isSeqStr(S) or !isSeqStr(T) or S.length + T.length > S.maxSize or pos < 1 or pos > S.length:
		return
	for x in range(T.length):
		S.add(T.data[x + 1], pos + x)
	return

def strDelete(S, pos, length):
	if !isSeqStr(S) or pos < 1:
		return
	if pos + length > S.length + 1:
		return
	for x in range(length):
		S.delete(pos)
	return
	

#test