def reinsertHoles(Y, idx, val=-99.0):
    '''
    Inputs:
        Y: A matrix without the excluded values
        idx: a vector with the position of excluded spectra
    Output:
        Yh: Matrix with 0.0 inserted in position of excluded values
    '''
    import copy as cp
    import numpy as np
    Yh = cp.copy(Y)
    n = 0  
    idx = list(np.array(idx).flatten())
    for n in range (0,len(idx)):
        Yh=np.insert(Yh, idx[n], val, axis=1)
    return Yh