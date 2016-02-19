#!/user/bin/env python
import numpy as np
import nibabel as nb
import random 
import sys

def size(A):
    i=[]
    while type(A)==list:
        i.append(len(A))
        A=A[0]
    return tuple(i)

def flatten(lst):
    """This function flattens a list"""
    return sum( ([x] if not isinstance(x, list) else flatten(x)
             for x in lst), [] )

def mygen(lst,s=slice(None)):
    for e in lst[s]:
        yield e

class Array(object):
    """ This is an Array class that represents arrays in n * lists 

    Methods:
    get_dimensions: returns dimensions of the array
    slic : slices the array
    checkdim : checks if all dimensions have equal rows and equal columns
    getelem: returns the element of the array

    """
    def __init__(self,data = None):
        self.data = data
        if data is None :
            self.data = [[]]
            pass
        elif isinstance(data,np.ndarray):
            self.data = data.tolist();
            if not self.checkdim():
                print " error: dimensions are not consistent"
            else:
                self.shape = data.shape
                self.dim = len(data.shape)
        elif not isinstance(data,list):
            print " Cannot parse input as Array "
            print " data must be a list "
        elif isinstance(data,list):
            if not self.checkdim():
                print " error: dimensions are not consistent"
            else:
                self.data = data
                self.shape = tuple(size(data))
                self.dim = len(self.shape)

    def get_dimensions ( self ):
        """ Returns the dimensions of the array as a tuple 
        Input
        ----------
        self : Array
        An array as a list of lists
        Returns
        -------
        s : tuple
        Dimensions of A
        """
        i,A=[],self.data
        while type(A)==list:
            i.append(len(A))
            A=A[0]
        return i

    def slic (self , slicelist):
        """ Slices an Array

        Inputs
        ----------
        self : Array
        slicelist: must be a list of slice objects with length equal dimensions

        Returns
        -------
        Sliced list

        Examples
        >> l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
        >> l = Matrix(l)
        >> l.slic([slice(0,2),slice(1,2),slice(0,2)])
        >> Out: [[[3, 4]], [[7, 8]]]
        --------
        """
        if self.dim==len(slicelist):
            # dimension is good
            for i in slicelist: # are each one slice objects?
                if not isinstance(i,slice):
                    print "error : you must enter slice objects"
                    return
            # start slicing
            if len(slicelist)==2:
                return [[j for j in mygen(e,slicelist[1])] for e in mygen(self.data,slicelist[0])]
            elif len(slicelist)==3:
                return [[[z for z in mygen(j,slicelist[2])] for j in mygen(e,slicelist[1])] for e in mygen(self.data,slicelist[0])]
            elif len(slicelist)==4:
                return [[[[l for l in mygen(k,slicelist[3])] for k in mygen(j,slicelist[2])] for j in mygen(e,slicelist[1])] for e in mygen(self.data,slicelist[0])]
            else:
                "error: that dimension is not supported"
        else: 
            # nope
            print "error : wrong dimensions"

    def checkdim(self):
        """This function checks the number of elements of a 
        flattened list and compares the value with the value from size
        to know if the dimensions are consistent
        Returns true if good
        Returns false if bad"""
        flat = flatten(self.data)
        s = size(self.data)
        j=1
        for i in s:
            j = j*i
        if len(flat)==j:
            # print "dimensons are good"
            return True
        else:
            print "error : dimensions must match"
            return False

    def getelem(self,idx):
        """ Get element from an array
        Inputs
        ----------
        self : Array
        slicelist: must be a list of slice objects with length equal dimensions

        Returns
        -------
        Sliced list

        Examples
        >> l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
        >> l = Matrix(l)
        >> l.slic([slice(0,2),slice(1,2),slice(0,2)])
        >> Out: [[[3, 4]], [[7, 8]]]
        --------
        """
        # check if index is consistent with size
        A = self.data
        if len(size(A)) == len(idx):
            tl = A
            for i,x in enumerate(idx):
                if isinstance(tl,list):
                    tl = tl[x]
            return tl
        else:
            print "error : dimensions must match"


class Matrix(Array): # inherits Array fields and methods
    # 2 dimensions
    # dot products etc. 
    def __init__(self,data = None):
        self.data = data
        self.dim = self.checkdim()

    def get_row(self,r=0):
        """ Return a single row from array A, specified by index r
        Inputs
        ----------
        self : Matrix
        r : int , optional ( default = 0)
        Index of row to be returned , if absent , returns first row
        Returns
        -------
        row : list
        """
        A = self.data
        A = zip(*A)
        return list(A[r])

    def get_col(self,r=0):
        """ return a single column from array A, specified by index c
        Inputs
        ----------
        self : Matrix
        c : int , optional ( default = 0)
        Index of column to be returned , if absent return first column
        Returns
        -------
        col : list
        """
        A = self.data
        return list(A[r])

    def rowmean(self,vec):
        """
        Computes the mean for each row 
        """
        numrows = len(vec)    
        numcols = len(vec[0]) 
        m_vec = []
        for i in range(0,numrows):
            sum = 0.0;
            for j in range(0,numcols):
                sum += vec[i][j]
            m_vec.insert(i,sum/numcols)
        return m_vec

    def mean(self):
        """
        Computes the mean of entire matrix
        """
        vec = self.data
        numrows = len(vec)    
        numcols = len(vec[0]) 
        m_vec = []
        sum = 0.0;
        for i in range(0,numrows):
            for j in range(0,numcols):
                sum += vec[i][j]
        m_vec = sum/(numrows*numcols)
        return m_vec

    def vmean(self, vec):
        """
        Computes the mean of vector vec
        """
        numrows = len(vec)    # 3 rows in your example
        sum = 0.0;
        for j in range(0,numrows):
            sum += vec[j]
        return sum/len(vec)

    def vnorm(self, a):
        """
        finds norm of vector
        """
        sumsq = 0.0;
        for i in range(0,len(a)):
            sumsq += a[i]**2 
        return sumsq**.5

    def dot(self,x,y):
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


    def vcorr(self,x,y):
        """
        Finds correlation of two vectors
        """
        ndot_xy, ssq_x, ssq_y = 0.0, 0.0, 0.0; 
        for i in range(0,len(x)):
            ndot_xy += (x[i]-self.mean(x))*(y[i]-self.mean(y))
            ssq_x += (x[i]-self.mean(x))**2
            ssq_y += (y[i]-self.mean(y))**2
        return ndot_xy/((ssq_x**.5)*(ssq_y**.5))

    def transpose(self,x):
        """
        Outputs transpose matrix
        """
        x_T = zip(*x)
        return x_T

    def corr(self,vec):
        """
        Finds correlation through dot product
        """
        dm=[[j-self.vmean(x) for j in x] for x in vec]
        ndm=[[y/self.vnorm(x) for y in x] for x in dm]
        return self.dot(self.transpose(ndm),ndm)


    def disp(self,max_rows=50,max_cols=20):
        """
        Display a nicely formatted string of array A
        Inputs
        ----------
        self : Matrix
        max_rows : int. optional ( default = 50)
        max_cols"""
        A = self.data
        if len(zip(*A)) > max_rows:
            for i in [0,1,2]:
                s=row2str(get_row(A,i))
                print str(s).rjust(2)
            print '.\n.\n.'
            for i in [-3,-2,-1]:
                s=row2str(get_row(A,i))
                print str(s).rjust(2)
        elif len(A) > max_cols: 
            for i in range(0,len(A[0])):
                B = get_row(A,i)
                for j in [0,1,2]:
                    print str(B[j]).rjust(2),
                print ' . . .',
                for j in [-3,-2,-1]:
                    print str(B[j]).rjust(2),
                print
        else:
            A = zip(*A)
            for i in A:
                for j in i:
                    print str(j).rjust(2),
                print

    def write(self,fn,sep=' '):
        """ Write a matrix to ascii text file , such that rows and columns
        may be simply parsed using standard tools .
        Inputs
        ----------
        self : Matrix
        fn : str
        sep : str , optional default = ' '
        Returns
        -------
        None
        """
        A = self.data
        f=file(fn,'a')
        A = zip(*A)
        for i in A:
            for j in i:
                f.writelines([str(j),str(sep),])
            f.writelines(str('\n'))
        f.close()

    def hstack (self, tup):
        """ Stacks arrays in a sequence horizontally ( column wise )
        Inputs
        ----------
        self : Matrix
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
        print self.data, tup
        ntup = self.data.append(tup)
        print ntup
        l = len(zip(*ntup[0]))
        for j in ntup:
            if l!=len(zip(*j)):
                print "error: dimensions don't match"
                return
        m = [];
        for i in range(0,len(ntup)):
            m.append(ntup[i])
        return m

    def vstack (self, tup ):
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
        tup = self.data.append(list(tup))
        l = len(tup[0])
        for j in tup:
            if l!=len(j):
                print "error: dimensions don't match"
                return
        m = [];
        for i in range(0,len(tup)):
            m.extend(zip(*tup[i]))
        return zip(*m)


class Dataset(Matrix):
    """
    Measure
    # FeatuerwiseMeasure: values for each column ( t, degree freedom, p-value, means)
    # SampleWiseMeasure: one result rows
    # Dataset Measure: one result per dataset

    # (1) An array or matrix that stores numeric data
    # (2) a : Dataset attributes (a dict ?)
    # (3) fa : Feature attributes : just the means of each row. not sure what else to do
    # (4) sa : Sample attributes: just the means of each column. not sure what else to do
    """
    a = {'subjectName':[],'sourceFN':[]}
    def __init__(self,data=None,a = a, sa=sa,fa=fa):
        self.data = data
        self.a = a
        self.sa = dict(zip(map(lambda x:x+1,range(len(self.data))),self.rowmean(self.data)))
        self.fa = dict(zip(map(lambda x:x+1,range(len(self.data[0]))),self.rowmean(zip(*self.data))))

    def map_to_nifti ( self ):
        pass
        """ assuming the Dataset attributes contain information to map the dataset
        back into the original space , this will return a Nibabel nifti dataset ,
        which can then be written to a file using nibabel ."""
