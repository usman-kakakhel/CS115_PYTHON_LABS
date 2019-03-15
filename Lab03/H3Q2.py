#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:49:53 2018

@author: BOI
"""

def isPrime(i):
	
	for a in range(2, int(math.sqrt(i)+1)):
		if((i % a) == 0):
			return False

	return True


def listPrimes(a,b):
	
	for num in range(a, b+1):
		if (isPrime(num)):
			print(num)

import math
a = int(input ("Enter the value of a: "))
while (a <= 1):
	a = int(input ("Enter the value of a above 1: "))
b = int(input ("Enter the value of b: "))
while (b <= a):
	a = int(input ("Enter the value of b above a: "))         
listPrimes(a,b)
