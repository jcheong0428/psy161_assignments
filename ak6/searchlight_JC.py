import nibabel as nb
import numpy as np
import scipy.spatial as sp
import math as math
from progressbar import ProgressBar

class dataset:
    '''
    This is the fMRI dataset as a numpy array
    self.data = data
    self.fa = feature attributes
    self.sa = sample attributes
    '''
    def __init__(self,data=None,fa=None,sa=None):
        self.data = data
        self.fa = fa
        self.sa = sa

def xyz2idx(coords,space):
    '''
    Converts coordinates in n-dim space to index in flattened space
    Input
    ----------
    coordinates : tuple of (x,y,z)
    space: tuple of space (80,80,43)

    Output
    ----------
    index in a flattened space
    '''
    return np.ravel_multi_index(coords,space)

def idx2xyz(idx,space):
    '''
    Converts index to coordinates in n-dim space
    Input
    ----------
    idx: number of index
    space: tuple of space (80,80,43)

    Output
    ----------
    (x,y,z) coordinates in space 
    '''
    return np.unravel_index(idx,space)

# Main Searchlight function 
def searchlight(subjID=None,radius = 10):
    '''
    This function runs a searchlight analysis on a single subject
    
    Input
    ----------
    subjID : string format ex: 's00'
    radius : default is 10 mm
    
    Output
    ----------
    ds : dataset with results 
    ds.corr_matrix: correlations for each run each sphere
    ds.crossRunMatrix: cross run correlations for each sphere
    '''
    # Function to load nibabel data goes here. 
    ds = None # dataset with all runs for a subject
    numRuns = 10

    if subjID == None:
        s = 's00'
    else:
        s = subjID

    path = '/Users/jinhyuncheong/psy161_assignments/ak6/preprocessed_data/' + s + '/perrun/' # path to file
    maskfn = '/Users/jinhyuncheong/psy161_assignments/ak6/preprocessed_data/'+s+'/preproc/brain_mask.nii.gz'
    # for loop to concatenate each run data to one big dataset, ds
    print 'Loading '+s+' data'
    pbar = ProgressBar()
    for runNum in pbar(range(1,numRuns+1)):
        fname = 'glm_stats_run%02d.nii.gz' % runNum # wildcard for filename
        d = nb.load(path + '/' + fname) # load the file to d
        Nx,Ny,Nz,t = d.shape # get shape of d

        # concatenate file to one big dataset, ds
        npd = d.get_data() # get the numpy array data
        for ti in range(t): # for each tr (=6, monkeys, lemurs, etc...)
            tr0 = npd[:,:,:,[ti]].flatten()
            if ds==None:
                ds = tr0
            else:
                ds = np.vstack((ds,tr0))
    # Make separate columns for runNum and condition (1~6)

    # Setting up my dataset Class 
    rows, voxels = ds.shape
    fa = {'conditions': np.array([1,2,3,4,5,6]*10),
     'runNum': np.repeat([1,2,3,4,5,6,7,8,9,10],6),
     'space' : (Nx,Ny,Nz),
     'numVox' : Nx*Ny*Nz,
     'voxSz' : 3,
     'maskfn': maskfn,
     'masksize' : None}
    sa = {'voxnum': [i for i in range(1,voxels+1)]}
    ds = dataset(ds,fa,sa) # make it into a dataset class

    # mask the data with subject's brain mask
    rawmask = nb.load(maskfn)
    rawmask = rawmask.get_data()
    brainmask = rawmask.flatten()
    ds.fa['masksize'] = sum(brainmask)

    ds.data = np.compress(brainmask,ds.data,axis=1)
    ds.sa['voxnum'] = np.compress(brainmask,ds.sa['voxnum'])

    '''MODULE 2: This might as well be a different function'''
    '''Now we should have one big dataset,ds, with all runs 
    The next section calculates neighbors for each voxel''' 

    voxSz = ds.fa['voxSz'] # 3 mm distant voxels center to center
    Nx,Ny,Nz = ds.fa['space'] # 80 80 43
    voxels = ds.sa['voxnum'] # 43825
    space = ds.fa['space'] # 80 80 43
    ds.neighbors = {}

    pbar = ProgressBar()
    print 'Calculating spheres for searchlight'
    for seedvoxel in pbar(voxels):
        # Sets up the space of the matrix
        seed = idx2xyz(seedvoxel,space) #get coordinates from seed voxel
        x, y, z = np.ogrid[-seed[0]:space[0]-seed[0], -seed[1]:space[1]-seed[1], -seed[2]:space[2]-seed[2]]
        mask_r = x*x + y*y + z*z <= radius*radius
        activation = np.zeros(space)
        activation[mask_r] = 1
        flatmask = activation.flatten() # flatten to 1 x 275200, save in flatmask
        # store the idx_in_sphere in some kind of dict
        ds.neighbors[seedvoxel] = np.compress(brainmask,flatmask) # restrict space to brain

    '''MODULE 3'''
    ''' Run the actual RSA correlation anaylsis for each voxel '''
    print 'Calculating RSA correlations on searchlight'
    ds.corr_matrix ={}
    pbar = ProgressBar()
    for seedvoxel in pbar(ds.neighbors):
        ds.corr_matrix.update({seedvoxel: {}})
        sphere = ds.neighbors[seedvoxel] # get sphere mask
        for runNum in range(1,numRuns+1):
            dat = ds.data[ds.fa['runNum']==runNum] # get run data
            sphere_data = np.compress(sphere,dat,axis=1) # take subset of data
            # runs a correlation on betas for each voxel
            # should return a 6 x 6 matrix
            corr_matrix = np.corrcoef(sphere_data) # get corr matrix
            ds.corr_matrix[seedvoxel].update({runNum : corr_matrix}) #update


    # Calculate cross run correlations
    ds.crossRunMatrix = {}
    pbar = ProgressBar()
    print 'Calculating RSA correlations across runs for each voxel'
    for seedvoxel in pbar(ds.corr_matrix):
        ms = None
        allrunmatrix = ds.corr_matrix[seedvoxel]
        for runNum,m in allrunmatrix.iteritems():
            m[m==1]=0
            if ms==None:
                ms = sp.distance.squareform(m)
            else:
                ms = np.vstack((ms,sp.distance.squareform(m)))
        # Transpose because rows are conditions and columns are observations(runs)
        # This gives a 15 x 15 matrix that shows a corrcoef. 
        corr_matrix = np.corrcoef(ms.T) 
        ds.crossRunMatrix[seedvoxel] = corr_matrix
        # vstack the matrices. 

    return ds


