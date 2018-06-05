#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'hash'

__author__ = 'lxp'

#《大话数据结构》365页

class HashTable(object):
	def __init__(self):
		self.elem = None
		self.count = None

	def initHashTable(self):
		self.count = int(input("count = "))
		self.elem = [None] * self.count
		return 

	def hash(self, key):
		return (key % self.count)

	def insertHash(self, key):
		addr = hash(key)
		while self.elem[addr] != None:
			addr = (addr + 1) % self.count
		self.elem[addr] = key
		return 

	def searchHash(self, key):
		addr = self.hash(key)
		while self.elem[addr] != key:
			addr = (addr + 1) % self.count
			if self.elem[addr] == None or addr == hash(key):
				print(key, "不存在")
				return
		print(key, "存在")
		return


#test
def test():
	H = HashTable()
	H.initHashTable()
	L = [1, 3, 4, 3, 2, 1, 5, 6, 7, 8]
	for l in L:
		H.insertHash(l)
	M = [5, 5, 3, 6, 7, 12, 0]
	for m in M:
		H.searchHash(m)
	return

if __name__ == '__main__':
	test()