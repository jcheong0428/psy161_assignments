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

def getrow(A,r):
	'''returns row r of A as a list'''
	A = zip(*A)
	return list(A[r])

def row2str(row):
	'''takes a row as a list returns it as a formatted string'''
	a = ''
	for i in range(len(row)):
		a = a+str(row[i])
		if i<len(row)-1:
			a = a+' '
	return a

def write2(A,fn):
	'''same as write but using getrow and row2str'''
	f=file(fn,'a')
	for i in range(0,len(A[0])):
		f.writelines([row2str(getrow(A,i)),str(' '),])
		f.writelines(str('\n'))
	f.close()

def disp2(A):
	'''same as disp but using getrow and row2str'''
	for i in range(0,len(A[0])):
		s=row2str(getrow(A,i))
		print str(s).rjust(2)

def slice(A,rowrange,colrange):
	'''returns a slice of the list'''
	return [[A[i][j] for j in range(rowrange[0],rowrange[1])] for i in range(colrange[0],colrange[1])]


