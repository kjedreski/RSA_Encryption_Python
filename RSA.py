#!/usr/bin/python
import sys
import math
import myUtility
#Developer: Kevin Jedreski
#Purpose: RSA Encryption
	
def fermatsTest(size):
	n = myUtility.generateLargeN(size)
	k=0
	#test for prime, if not regen a random number.
	#pow(x,n)%z is inefficient and pow(x,n,z) computes more efficiently
	while( k<5):
			x = myUtility.generateInt(n)
			if (pow(x,n-1,n) == 1):
				k+=1
			else:
				n = myUtility.generateLargeN(size)
				k=0
	return n	

### retrieves ax+by=1
def Extended_Euclidean2(a,b):
	if (b==0):
		return (a,1,0)
	(d,x,y)=Extended_Euclidean2(b,a%b)
	(d,x,y)=(d,y,x-(a/b)*y)
	print "{}*{}+{}*{}=1".format(a,x,b,y)
	
# a = phi(n)
# b = e
def Extended_Euclidean(a,b):
	#return 2 integers such that gcd(a,b) = ax+by and y>0
	#init
	tempPhi1 = a #reps first column/first row and/or orig phi
	tempPhi2 = a #reps second column/first row and/or orig phi
	tempE = b #reps first column/second row and/or original e
	strt = 1 #reps second column/second row 
	#(strt*b)%a!=1 test case for while loop
	while( (strt*b)%a!=1 and tempE!=0 ):
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
	#return for ax+by=gcd(a,b)
	return d

def calcPhi_and_N(e,p,q):
	n=p*q
	phi=((p-1)*(q-1))
	
	if (myUtility.gcd(phi,e)>1):
		e+=2
	return n,phi,e
	
def RSA_Encryption(e,n,message): #int pair, public key string and
	#message to be encrypted
	M=""
	for c in message:
		if (len(str(ord(c)))==2):
			c=str(ord(c))
			c = str(c).zfill(3)
			M+=c
		#elif (len(str(ord(c)))==1):
		#	c=str(ord(c))
		#	t1
		else:
			M+=str(ord(c))
	M=int(M)
	#convert string t3o ascii string
	#then convert back to int
	# M = 10734553
	print M
	C=pow(M,e,n)
	return C

def RSA_Decrpytion(d,n,message):
	#convert num to asci code
	# ord() text to ascii
	# chr() ascii to text
	#parse from the back,
	
	
	print "In Decrpytion func, encrypted message is {}".format(message)
	M=pow(message,d,n)
	print "Using private key, ascii value should be: {}".format(M)
	answer=""
	while (M>0):
		#make a list and then join
		answer+=chr(M%1000)
		M/=1000
	result = ""
	for i in xrange(len(answer)-1,-1,-1):
		result+= answer[i]
	print result
	#parse every 3 digits from ascii msg
	#while (i <= msgLen):
	# append from begining to position 3
	#	values.append(M[:3])
	#append from position 3 to end
	#	M = M[3:]
	#	i+=3
	#for i in values:
	#	answer+=chr(int(i))
	return result
		
	
def main():
	#argparse treats it as strings
	numArgs = len(sys.argv)
	argList = sys.argv
	#build a switch case funct
	if (numArgs == 2):
		s = int(argList[1])
		print fermatsTest(s)
	elif (numArgs == 3):
		a = int(argList[1])
		b = int(argList[2])
		Extended_Euclidean2(a,b)
	elif (numArgs == 4):
		e=int(argList[1])
		p=int(argList[2])
		q=int(argList[3])
		n,phi,e = calcPhi_and_N(e,p,q)
		d=Extended_Euclidean(phi,e)
		print 'n is {}'.format(n)
		print 'phi={}'.format(phi)
		print 'e={}'.format(e)
		print 'd={}'.format(d)
	elif (numArgs == 5):
		if (argList[1]=='e'):
			e=int(argList[2])
			n=int(argList[3])
			message=argList[4]
			print RSA_Encryption(e,n,message)
		elif (argList[1]=='d'):
			d=int(argList[2])
			n=int(argList[3])
			message=int(argList[4])
			print RSA_Decrpytion(d,n,message)
			
			
main()
#test cases
#
#p=fermatsTest(100)
#q=fermatsTest(100)
#e=11
#n,phi,e=calcPhi_and_N(e,p,q)
#above are checked off and working
#d=Extended_Euclidean(phi,e)
#when doing modular arithmetic, you cannot get a result greater or equal than
#modulus
#print '{}*{}+{}*{}=1'.format(phi,x,e,y)
#print d,x,y
#d is the inverse of e, hence showing original message
#message= raw_input('message you want to encrypt is: ')
#C=RSA_Encryption(e,n,message)
#print 'C is {}'.format(C)
#RSA_Decrpytion(d,n,C)
#print answer
