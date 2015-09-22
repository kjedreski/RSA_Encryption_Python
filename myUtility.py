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
	
#generate a relatively prime number
#a   Large N prime number, 
def generateE(a,b):
	#e has to be relatively prime of phi
	e = random.randint(3,65537)
	while ( gcd(e,b)!=1 and gcd(b,e)!=1):
		e = random.randint(3,65537)
	return e
	#conditions: a and e are positive
	
#returns greatest common divisor 
def gcd(a,b):
	if (b == 0):
		return a
	else:
		return gcd(b,a % b)