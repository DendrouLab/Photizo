def selectRegionY(x0, x1, X, Y):
    '''
    Inputs:
        x0: Starting wavelength of interest
        x1: Ending wavelength of interest
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        
    Output:
        Y: Matrix subset within given spectral region between x0 and x1 wavelengths
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    
    a0 = bracketPoint(x0, X)
    a1 = bracketPoint(x1, X)

    return Y[a0:a1,:]
