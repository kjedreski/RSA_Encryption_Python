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



	

# a = phi(n)
# b = e
def Extended_Euclidean(a,b):
	# ('first_int':x,'sec_int':y)
	#ax%M=1
	#return 2 integers such that gcd(a,b) = ax+by and y>0
	
	#init
	tempPhi1 = a #reps first column/first row and/or orig phi
	tempPhi2 = a #reps second column/first row and/or orig phi
	tempE = b #reps first column/second row and/or original e
	strt = 1 #reps second column/second row 
	
	#loop
	#conditions:: tempE is 1
	#e*d mod b =1 
	#check for negatives
	#
	#
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
	print 'strt= %r, tempPhi1=%r, tempE=%r'%(strt,tempPhi1,tempE)
	
	#logic 
	#init
	#  tempPhi1 = a this represents phi
	# tempPhi2 = a
	# tempE = b this represents E
	# strt = 1 this represents 1
	
	#loop
	#first divide tempPhi by e = result
	#result = tempPhi/e
	#multiply result * tempE and result*strt for res1 and res2
	#s1 and s2 will equal strt and tempE
	# subtract tempE=tempPhi1-res1 and strt=tempPhi2-res2
	#tempPhi1 = s1 amd tempPhi2 =s2
	#repeat process
	
	#ending conditions when tempE is 1 then strt is 'd'
	#e*d mod b =1 
	
	#validations: if negative -> (x=negative) ->y=xmoda 
	
	
	
	
	
	
def RSA_Encryption(e,n): #int pair, public key string and
	#message to be encrypted
	return 'some string'
	
	
	
	#during main course, validate size to be not 0
	#MAIN
	#variables we have: p and q.
	#we have e.
	#we need n,phi and d
print fermatsTest(3)
Extended_Euclidean(40,7)


		