#!/user/bin/env python

import random as rand 

def make_rand_array(n,m):
	'''Make random array of size n x m with values from 1 to 10'''
	return [[rand.randint(1,10) for j in range(0,m)] for i in range(0,n)]

def fmake_rand_array(n,m):
	'''Same as make_rand_array with for loop'''
	A =[]
	for i in range(n):
		col = []
		for j in range(m):
			col.append(rand.randint(1,10))
		A.append(col)
	return A

def size(A):
	'''returns a tuple (n,m)'''
	return (len(A[0]),len(A))

def disp(A):
	'''prints a neatly formatted version of A to stdout'''
	A = zip(*A)
	for i in A:
		for j in i:
			print str(j).rjust(2),
		print

def write(A,fn):
	'''writes A to file f as ASCII test'''
	f=file(fn,'a')
	A = zip(*A)
	for i in A:
		for j in i:
			f.writelines([str(j),str(' '),])
		f.writelines(str('\n'))
	f.close()