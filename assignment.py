#!/user/bin/env python
a = [1,2,3,4,5,1,2,3,4,5]
b = [-1,1,5,6,7,5,6,7,8,9]
A = [[ 1, 2, 3],[ 4, 5, 6]]

def mean(a):
	sum = 0.0;
	for i in range(0,len(a)):
		sum += a[i]
	return sum/len(a)

def var(a):
	m = mean(a);
	sumsq = 0.0;
	for i in range(0,len(a)):
		sumsq += (a[i]-m)**2
	return sumsq/(len(a)-1)

def stdev(a):
	v = var(a)
	return v**.5

def corr(x,y):
	sum_dxdy = 0.0;
	for i in range(0,len(x)):
		sum_dxdy += (x[i]-mean(x))*(y[i]-mean(y))
	covar = sum_dxdy/(len(x)-1)
	return covar /((var(x)*var(y))**.5)

def norm(a):
	sumsq = 0.0;
	for i in range(0,len(a)):
		sumsq += a[i]**2 
	return sumsq**.5

def dot(x,y):
	sum_xy = 0.0;
	for i in range(0,len(x)):
		sum_xy += x[i]*y[i]
	return sum_xy

def vcorr(x,y):
	ndot_xy, ssq_x, ssq_y = 0.0, 0.0, 0.0; 
	for i in range(0,len(x)):
		ndot_xy += (x[i]-mean(x))*(y[i]-mean(y))
		ssq_x += (x[i]-mean(x))**2
		ssq_y += (y[i]-mean(y))**2
	return ndot_xy/((ssq_x**.5)*(ssq_y**.5))

def transpose(x):
	x_T = zip(*x)
	return x_T

def sqrt(x):
	return x**.5

print "Average: ", mean(a)
print "Variance: ",var(a)
print "Standard deviation: ",stdev(a)
print "Pearson correlation: ",corr(a,b)
print "Vector method Pearson Correlation: ",vcorr(a,b)
print "Square root: ",sqrt(2)
print "Norm of a vector: ",norm(a)
print "Dot product of two vectors: ",dot(a,b)
print "Transpose: ",transpose(A)