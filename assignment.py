#!/user/bin/env python
"""
License information goes here. 

Making functions on the fly 
f= lambda x: x**2
map(f,list) : take each value of list and do operation on it
[func(x) for x in list]  : comprehensive list 

nested list comprehension 
x_T = [[ col[row] for col in X ] for row in range(nrow) ]

"""
a = [1,2,3,4,5,1,2,3,4,5]
b = [-1,1,5,6,7,5,6,7,8,9]
A = [[ 1, 2, 3],[ 4, 5, 6]]
M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
M2 = [[5, 2, 7, 4], [3, 2, 7, 8], [8, 22, 1, 15]]
def sum(vec): 
	"""
	Computes the sum of vector vec
	"""
	sum = 0.0;
	numrows = len(vec) 
	for j in range(0,numrows):
		sum += vec[j]
	return sum

def vmean(vec):
	"""
	Computes the mean of vector vec
	"""
	numrows = len(vec)    # 3 rows in your example
	sum = 0.0;
	for j in range(0,numrows):
		sum += vec[j]
	return sum/len(vec)

def mean(vec):
	"""
	Computes the mean of matrix
	"""
	numrows = len(vec)    # 3 rows in your example
	numcols = len(vec[0]) # 2 columns in your example
	m_vec = []
	for i in range(0,numrows):
		sum = 0.0;
		for j in range(0,numcols):
			sum += vec[i][j]
		m_vec.insert(i,sum/numcols)
	return m_vec

def var(a):
	"""
	Computes the variance of vector vec
	"""
	m = mean(a);
	sumsq = 0.0;
	for i in range(0,len(a)):
		sumsq += (a[i]-m)**2
	return sumsq/(len(a)-1)

def stdev(a):
	"""
	finds standard deviation
	"""
	v = var(a)
	return v**.5

def scorr(x,y):
	"""
	finds correlation of two vector
	"""
	sum_dxdy = 0.0;
	for i in range(0,len(x)):
		sum_dxdy += (x[i]-mean(x))*(y[i]-mean(y))
	covar = sum_dxdy/(len(x)-1)
	return covar /((var(x)*var(y))**.5)

def norm(a):
	"""
	finds norm of matrix per column
	"""
	sumsq = 0.0;
	for i in range(0,len(a)):
		for j in range(0,len(a[0])):
			sumsq += a[i][j]**2 
	return sumsq**.5

def vnorm(a):
	"""
	finds norm of vector
	"""
	sumsq = 0.0;
	for i in range(0,len(a)):
		sumsq += a[i]**2 
	return sumsq**.5

def dot(x,y):
	"""
	finds dot product of two matrix
	"""
	numrows = len(x[0])
	numcols = len(x)
	dot_xy = []
	for i in range(0,numrows):
		ssum_xy =[];
		for k in range(0,numrows):
			sum_xy = 0.0;
			for j in range(0,numcols):
				sum_xy += x[j][i]*y[k][j]
			ssum_xy.append(sum_xy)
		dot_xy.append(ssum_xy)
	return dot_xy

def vcorr(x,y):
	"""
	Finds correlation of two vectors
	"""
	ndot_xy, ssq_x, ssq_y = 0.0, 0.0, 0.0; 
	for i in range(0,len(x)):
		ndot_xy += (x[i]-mean(x))*(y[i]-mean(y))
		ssq_x += (x[i]-mean(x))**2
		ssq_y += (y[i]-mean(y))**2
	return ndot_xy/((ssq_x**.5)*(ssq_y**.5))

def transpose(x):
	"""
	Outputs transpose matrix
	"""
	x_T = zip(*x)
	return x_T

def sqrt(x):
	"""
	Calculates square root
	"""
	return x**.5

def corr(vec):
	"""
	Finds correlation through dot product
	"""
	dm=[[j-vmean(x) for j in x] for x in vec]
	ndm=[[y/vnorm(x) for y in x] for x in dm]
	return dot(transpose(ndm),ndm)

	

# print "Average: ", mean(M)
# print "Transpose: ",transpose(M)
# M_T = transpose(M)
# print "Dot product: ", dot(M_T,M)
# print 'Correlation matrix: ', corr(M2)
# print "Correlation: ", corr(M)
# print "Variance: ",var(M)
# print "Standard deviation: ",stdev(a)
# print "Pearson correlation: ",corr(a,b)
# print "Vector method Pearson Correlation: ",vcorr(a,b)
# print "Square root: ",sqrt(2)
# print "Norm of a vector: ",norm(a)


# print "Dot product of two vectors: ",dot(M_T,M)