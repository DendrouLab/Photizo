def alphaHelix(X, Y):
    '''
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        
    Output:
        % contribution of alpha-helix folding based on method described by Goormaghtigh et al, 2009
    '''
    
    from photizo.preprocessing.bracketPoint import bracketPoint
    from photizo.quantification.nIntegrate import nIntegrate
    
    Area = nIntegrate(1481, 1725, X, Y) 
    NormY = (Y/Area)*10000
    A1654 = bracketPoint(1654, X)
    A1588 = bracketPoint(1588, X)
    A1546 = bracketPoint(1546, X)
    
    return -148.10 + 0.98*NormY[A1654, :] + 1.49*NormY[A1588, :] + 0.66*NormY[A1546, :]
