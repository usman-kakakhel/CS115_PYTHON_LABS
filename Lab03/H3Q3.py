#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:49:53 2018

@author: BOI
"""

def throwUntil(x):
	import random
       
	sumDice = 0
	tries = 0

	while sumDice != x:
	    
		try1 = random.randint (1,7)
		try2 = random.randint (1,7)
             
		sumDice = try1 + try2
		tries += 1
            
		if sumDice == x:    
			print ("Die1: {}  Die2: {}".format(try1, try2))
            
	return tries

x = int(input ("Enter the sum of dice: ")) 
while x <= 1 or x > 12:
	print ("Sum must be between 2 and 12 inclusive")
	x = int(input ("Enter the sum of dice: ")) 
          
tries = throwUntil(x)
print ("Dices are rolled {} times to get the sum {}".format (tries ,x))
