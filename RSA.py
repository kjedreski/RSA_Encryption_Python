#!/usr/bin/python
import sys
import math
import myUtility
#Developer: Kevin Jedreski
#Purpose: RSA Encryption
# There's a 1/25 chance to grab a random prime
# According to Langrange's prime number theory they are abundant
#		  fermatsTest:
#		     n to test , k will be how many times to test for primility,
#		    repeat k times

	
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
	#return for ax+by=gcd(a,b)
	return d,tempE

def calcPhi_and_N(e,p,q):
	n=p*q
	phi=((p-1)*(q-1))
	
	return n,phi
	
	
	
def RSA_Encryption(e,n,message): #int pair, public key string and
	#message to be encrypted
	M=""
	for c in message:
		M+=str(ord(c))
	M=int(M)
	#convert string to ascii string
	#then convert back to int
	# M = 10734553
	C=pow(M,e,n)
	return C

def RSA_Decrpytion(d,n,message):
	#convert num to asci code
	M=pow(message,d,n)
	answer = ""
	while (M>0):
		answer+=str(ord(M%128))
		M/=128
	
	#now answer should be in ascii, we need to convert to chars
	return answer

	#m%128 -> last char
	#m/=128
	
	
	
#during main course, validate size to be not 0
#MAIN
#variables we have: p and q and e and d
#we need n,phi 
# n is p*q and phi is (p-1)*(q-1)
#Next task, build the command line parser
#		cases:
#				script.exe s
#				script.exe a b
#				script.exe e p q
#				script.exe 'e' e n
#				script.exe 'd' d n




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
		print myUtility.gcd(a,b)
			
	elif (numArgs == 4):
	    if (argList[2]=='p'):
			print 'found e p q'
			e=argList[1]
			p=argList[2]
			q=argList[3]
			Extended_Euclidean(e,p*q)
			
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
			
	
	

#print fermatsTest(3)
#Extended_Euclidean(40,7)

#fermatsTest(10)
#main()


#test cases
p=fermatsTest(10)
q=fermatsTest(10)
e=7
n,phi=calcPhi_and_N(e,p,q)
d,temp= Extended_Euclidean(phi,e)
message= raw_input('message you want to encrypt is: ')
C=RSA_Encryption(e,n,message)
#answer=RSA_Decrpytion(d,n,C)
#print answer




#numArgs = len(sys.argv)
#	argList = str(sys.argv)
#	print sys.argv[1]
#	print argList
#	if (numArgs == 2):
#		print '2 arguments!'
#	elif (numArgs == 3):
#		print '3 arguments!'
#
#
#
#
#
#
#
#
#








		