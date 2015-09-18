import math
import myUtility
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

def Extended_Euclidean(a,b):
	return 3# ('first_int':x,'sec_int':y)
	#return 2 integers such that gcd(a,b) = ax+by and y>0
	
def RSA_Encryption(e,n): #int pair, public key string and
	#message to be encrypted
	return 'some string'
	
	
	
	#during main course, validate size to be not 0
	#MAIN
	
print fermatsTest(3)
	
		