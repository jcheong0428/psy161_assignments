#!/user/bin/env python

import random as rand 

def make_rand_array(dims,start=0,stop=10,dt='int'):
	""" make_rand_array (dims , start =0 , stop =10 , dtype = 'int')
	Returns an array of random values size specified in the tuple
	dims , i.e. , an array of size n X m for dims = (n,m)
	Parameters
	----------
	dims : tuple of ints
	start : int , optional ( default 0)
	stop : int , optional ( default 10)
	dt : str { int , float } , optional ( default int)
	Returns
	-------
	A : list of lists containing random numbers . Length of outer
	"""
	m = [[rand.randint(start,stop) for j in range(0,dims[1])] for i in range(0,dims[0])]
	if dt == 'float':
		n =[]
		for i in m:
			n.append(list(map(float,i)))
		m=n
	return m

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
	""" Returns the size of array A
	Parameters
	----------
	A : list
	An array as a list of lists
	Returns
	-------
	s : tuple
	Dimensions of A
	"""
	return (len(A[0]),len(A))

def disp(A):
	"""
	Display a nicely formatted string of array A
	Parameters
	----------
	A : list
	max_rows : int. optional ( default = 50)
	max_cols : int , optional ( default = 20)
	"""
	A = zip(*A)
	for i in A:
		for j in i:
			print str(j).rjust(2),
		print

def write(A,fn,sep=' '):
	""" Write a matrix to ascii text file , such that rows and columns
	may be simply parsed using standard tools .
	Parameters
	----------
	A : list
	fn : str
	sep : str , optional default = ' '
	Returns
	-------
	None
	"""
	f=file(fn,'a')
	A = zip(*A)
	for i in A:
		for j in i:
			f.writelines([str(j),str(sep),])
		f.writelines(str('\n'))
	f.close()

def get_row(A,r=0):
	""" Return a single row from array A, specified by index r
	Parameters
	----------
	A : list
	An array
	r : int , optional ( default = 0)
	Index of row to be returned , if absent , returns first row
	Returns
	-------
	row : list
	"""
	A = zip(*A)
	return list(A[r])

def get_col(A,r=0):
	""" return a single column from array A, specified by index c
	Parameters
	----------
	A : list
	An array
	c : int , optional ( default = 0)
	Index of column to be returned , if absent return first column
	Returns
	-------
	col : list
	"""
	return list(A[r])

def row2str(row,sep=' '):
	""" Return a nicely formatted sting of matrix row r
	Parameters
	----------
	r : list
	sep : str , optional, default = ' '
	Returns
	-------
	row : str
	"""
	a = ''
	for i in range(len(row)):
		a = a+str(row[i])
		if i<len(row)-1:
			a = a+sep
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
	""" Return specified sub - portion of array A
	Parameters
	----------
	A : list
		An Array
	rowrange : list
		List of row indices ( ints ) specifying rows to be included in returned
		slice
	colrange : list
		List of column indices ( ints ) specifying columns to be returned
	Returns
	-------
	S : list
	An array which is the sliced version of A
	"""
	return [[A[i][j] for j in range(rowrange[0],rowrange[1])] for i in range(colrange[0],colrange[1])]

def get_elem (A, i, j):
	""" Return the value of A at indices row i and column j
	Parameters
	----------
	A : list
	i : int
	j : int
	Returns
	-------
	v : int or float
	"""
	return A[j][i]

def hstack (tup ):
	""" Stacks arrays in a sequence horizontally ( column wise )
	Parameters
	----------
	tup : tuple
	This is a sequence of array that must have the same number of
	rows , number of columns may differ
	Returns
	-------
	H : list
	An array
	Notes
	-----
	For input tup = (A, B, C) , with sizes : A = (3 ,2) , B = (3 ,2) , C =
	3 ,1) , hstack returns array H with size H = (3 ,5)
	Examples
	8
	--------
	>>> a = [[1 ,2 ,3] ,[4 ,5 ,6]]
	>>> b = [[9 ,8 ,7] ,[6 ,5 ,4]]
	>>> c = [[3 ,4 ,5]]
	>>> hstack ((a,b,c))
	[[1 ,2 ,3] ,[4 ,5 ,6] ,[9 ,8 ,7] ,[6 ,5 ,4] ,[3 ,4 ,5]]
	"""
	l = len(zip(*tup[0]))
	for j in tup:
		if l!=len(zip(*j)):
			print "error: dimensions don't match"
			return
	m = [];
	for i in range(0,len(tup)):
		m.append(tup[i])
	return m

def vstack (tup ):
	""" Vertically stacks a sequence of arrays (row wise )
	Parameters
	----------
	tup : tuple
	A sequence of arrays that must have the same number of columns
	Returns
	-------
	V : list
	An array .
	Examples
	--------
	>>> a = [[1 ,2] ,[3 ,4] ,[5 ,6]]
	>>> b = [[9] ,[8] ,[7]]
	>>> c = [[4 ,5] ,[6 ,7] ,[8 ,9]]
	>>> V = vstack ((a,b,c))
	>>> V
	[[1 ,2 ,9 ,4 ,5] ,[3 ,4 ,8 ,6 ,7] ,[5 ,6 ,7 ,8 ,9]]
	"""
	l = len(tup[0])
	for j in tup:
		if l!=len(j):
			print "error: dimensions don't match"
			return
	m = [];
	for i in range(0,len(tup)):
		m.extend(zip(*tup[i]))
	return zip(*m)
