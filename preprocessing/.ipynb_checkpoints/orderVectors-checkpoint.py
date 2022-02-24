def orderVectors(X, Y):
    '''
    Inputs:
        X: Vector containing wavelengths
        Y: Matrix containing all spectra
        
    Output:
        Xnew: Reordered vector containing wavelengths in ascending order
        Ynew: Reordered matrix according to reordered wavelengths
    '''
    import operator
    import numpy as np
    L = sorted(zip(X,Y), key=operator.itemgetter(0))
    Xnew, Ynew = zip(*L)
    return Xnew, np.array(Ynew)
