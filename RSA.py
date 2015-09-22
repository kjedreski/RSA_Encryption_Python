import math
import myUtility
import sys
#Developer: Kevin Jedreski
#Purpose: RSA Encryption
# There's a 1/25 chance to grab a random prime
# According to Langrange's prime number theory they are abundant
#		  fermatsTest:
#		     n to test , k will be how many times to test for primility,
#		    repeat k times
#
#
#
	
def fermatsTest(size):
	n = myUtility.generateLargeN(size)	
	k=0
	#test for prime, if not regen a random number.
	while( k<5):
			x = myUtility.generateInt(n)
			if (pow(x,n-1)%n == 1):
				k+=1
			else:
				n = myUtility.generateLargeN(size)
				k=0	
	return n	

# a = phi(n)
# b = e
def Extended_Euclidean(a,b):
	#return 2 integers such that gcd(a,b) = ax+by and y>0
	#init
	tempPhi1 = a #reps first column/first row and/or orig phi
	tempPhi2 = a #reps second column/first row and/or orig phi
	tempE = b #reps first column/second row and/or original e
	strt = 1 #reps second column/second row 
	while( (strt*b)%a!=1 ):
		res=tempPhi1/tempE
		res1= res*tempE
		res2=res*strt
		s1=tempE
		s2=strt
		tempE=tempPhi1-res1
		strt=tempPhi2-res2
		tempPhi1 = s1
		tempPhi2 = s2
		if (strt<0):
			strt %=a
	d = strt
	# return d which is y. return quotient which is x		
	print 'strt= %r, tempPhi1=%r, tempE=%r'%(strt,tempPhi1,tempE)
	#return for ax+by=gcd(a,b)
	return d,tempE

	
	
	
	
	
	
def RSA_Encryption(e,n): #int pair, public key string and
	#message to be encrypted
	return 'some string'
	
	
	
#during main course, validate size to be not 0
#MAIN
#variables we have: p and q and e and d
#we need n,phi 
# n is p*q and phi is (p-1)*(q-1)
#Next task, build the command line parser
print fermatsTest(3)
Extended_Euclidean(40,7)






		