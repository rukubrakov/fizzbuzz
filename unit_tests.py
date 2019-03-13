#!/usr/bin/python3

import unittest
from fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz(self):
		B, A = [], []
		i = 0
		with open('tests.txt') as file:
			for line in file:
				A.append(line)
				B.append(line)
				++i
		for e in range(i):
			f = fizz(A[e])
			self.assertEqual(f, B[e])

if __name__=="__main__":
	unittest.main()
