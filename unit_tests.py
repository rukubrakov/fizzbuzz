#!/usr/bin/python3

import unittest
from fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz(self):
		B, A = [], []
		i = 0
		with open('tests.txt') as file:
			for line in file:
				if i % 2 == 0:
					A.append(line)
				else:
					B.append(line)
				i = i + 1
		for e in range((int)(i/2)):
			f = fizz(A[e])
			self.assertEqual(f, B[e])

if __name__=="__main__":
	unittest.main()
