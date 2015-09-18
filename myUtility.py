import random
import math
#Developer: Kevin Jedreski
#Purpose: Utility functions for RSA encryption

#generate random large number thats @size digits long and odd
def generateLargeN(size):
	start = 2*pow(10,size-1)
	end = 9*pow(10,size-1)
	n = random.randint(start,end)
	while (n%2 == 0):
		n = random.randint(start,end) 
	return n
#generate a integer for fermat's test
def generateInt(n):
	return random.randint(2,n-2)