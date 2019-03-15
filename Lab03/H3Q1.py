#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:49:53 2018

@author: BOI
"""

def grid(n):
	import random
	
	for x in range(n):
		for i in range(n):
			print (random.randint (0,1), end=" ")
		
		print("") 
    

n = int(input ("Enter the value of n: ")) 
          
grid(n)
