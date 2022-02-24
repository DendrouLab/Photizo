def betaTurn(X,Y):
    '''
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        
    Output:
        % contribution of Beta-turn folding based on method described by Goormaghtigh et al, 2009
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    from photizo.quantification.nIntegrate import nIntegrate
    
    Area = nIntegrate(1481, 1725, X, Y) 
    NormY = (Y/Area)*10000   
    A1678 = bracketPoint(1678, X)
    A1501 = bracketPoint(1501, X)
    
    return -14.25 + 0.36*NormY[A1678, :] + 0.85*NormY[A1501, :]
