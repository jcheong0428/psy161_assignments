#!/user/bin/env python
import numpy as np
import random 
import sys

def size(A):
    i=[]
    while type(A)==list:
        i.append(len(A))
        A=A[0]
    return tuple(i)

def flatten(lst):
    """"This function flattens a list"""
    return sum( ([x] if not isinstance(x, list) else flatten(x)
             for x in lst), [] )

def checkdim(A):
    """This function checks the number of elements of a 
    flattened list and compares the value with the value from size
    to know if the dimensions are consistent"""
    flat = flatten(A)
    s = size(A)
    j=1
    for i in s:
        j = j*i
    if len(flat)==j:
        print "dimensons are good"
    else:
        print "error : dimensions are not equal"

def mygen(lst,s=slice(None)):
    for e in lst[s]:
        yield e

class Array(object):
    """
    Attributes:
    """

    def __init__(self,data = None):
        """Return a new Truck object."""
        self.data = data
        if data is None :
            self.data = [[]]
            pass
        elif isinstance(data,np.ndarray):
            self.data = data.tolist();
            self.shape = data.shape
            self.dim = len(data.shape)
        elif not isinstance(data,list):
            print " Cannot parse input as Array "
            print " data must be a list "
        elif isinstance(data,list):
            self.data = data
            self.shape = tuple(size(data))
            self.dim = len(self.shape)
        # (1) Next Check if how many dimensions
        # not implemented
        # the self . shape field should be a tuple with dimensions
        # starting with rows , then column , etc.
        # implemented above with size()

        # (2) Check to see that each element of each dimension
        # has the right number of sub - elements
        # ie. make sure each column has the right number of rows ...
        # write this for N- dimensional arrays

    def get_dimensions ( self ):
        """ Returns the dimensions of the array as a tuple 
        Parameters
        ----------
        A : list
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

    def slice (self , *args):
        """ Return sliced version of array with specified
        rows and columns """
        if self.dim==len(args):
            # dimension is good
            for i in args: # are each one tuples?
                if not isinstance(i,tuple):
                    print "error : you gotta tuple"
                    return
            # start slicing

        else: 
            # nope
            print "error : wrong dimensions"
        
        # Please add any or all methods derived from the functions in 5 ( above ) that
        # make sense to have as Array methods


class Matrix(Array): # inherits Array fields and methods
    def __init__(self,data = None):
        self.data = data



class Dataset(Matrix):
    def __init__(self,data=None,sourcefn=None):
        self.data = data
		#dictionary fa, sa
		#sa = {'conds'=[...list...]; (constraint:matching rows),...
		#'runs'=[...list...]}

# Measure
# FeatuerwiseMeasure: values for each column ( t, degree freedom, p-value, means)
# SampleWiseMeasure: one result rows
# Dataset Measure: one result per dataset
