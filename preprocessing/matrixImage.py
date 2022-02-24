def matrixImage(sqrsx, sqrsy, Y0):
    '''
    This function reshapes a vector into the given matrix dimensions

    Inputs:
        sqrsx: Number of pixels in the X axis
        sqrsy: Number of pixels in the Y axis
        Y0: Vector containing cluster classification of all pixels of a sample. This vector must have a value of -99 inserted in the positions where spectra were excluded.
    
    Output:
        returns matrix of cluster classification in given coordinates
'''
    import numpy as np
    count=0
    mat = np.zeros(shape=(sqrsy,sqrsx))
    for m in range (0,sqrsy):
        for n in range (0,sqrsx):
            mat[m,n]=Y0[count]
            count+=1
    return mat
