def size(A):
    i=[]
    while type(A)==list:
        i.append(len(A))
        A=A[0]
    return tuple(i)

def slicer(lst,slicelist,i=0):
    res = []
    if isinstance(slicelist,slice):
        return res
    else:
        print lst, slicelist,
        for i,e in enumerate(lst[slicelist[i]]):
            print i,e
            res.append(slicer(e,slicelist(i),i))

def mygen2(lst,slicelist):
    """ Returns a slice of your Array. 
    Input must be a list of tuples with length the same as dimensions. 
    Only supports 2 ~ 4 dimensions right now...

    Examples
    --------
    >> a=[[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
    >> A = Array(a)
    >> A.mygen2([slice(0,2),slice(0,2),slice(0,2)])

    >> [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    maybe use res.append(recursive function here)
    """
    res = []
    if isinstance(lst,list)&isinstance(slicelist,list):
        s = slicelist[0]
        for e in lst[s]:
            res.append(list(slicer(e,s)))
            lst = list(slicer(e,s))
        slicelist.pop(0)
    return res