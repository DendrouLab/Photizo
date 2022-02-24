def removeCO2(X, Y):
    '''
    Inputs:
        X: a vector with wavelengths
        Y: a matrix with all spectra
        
    Output:
        X: Modified wavelength vector which does not include 2,250-2,400 spectral region
        Y2: Modified spectral matrix which does not include 2,250-2,400 spectral region
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    import numpy as np
    
    a0 = bracketPoint(2250, X)
    a1 = bracketPoint(2400, X)
    Y[a0:a1,:]
    Ya = Y[0:a0,:]
    Yb = Y[a1:,:]
    Y2 = np.concatenate((Ya, Yb), axis = 0)

    Xa = X[0:a0]
    Xb = X[a1:]
    X = np.concatenate((Xa, Xb), axis = 0)
    
    return X, Y2
