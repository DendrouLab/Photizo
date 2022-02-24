def betaSheet(X,Y):
    '''
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        
    Output:
        % contribution of beta-sheet folding based on method described by Goormaghtigh et al, 2009
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    from photizo.quantification.nIntegrate import nIntegrate
    
    Area = nIntegrate(1481, 1725, X, Y) 
    NormY = (Y/Area)*10000  
    A1657 = bracketPoint(1657, X)
    A1629 = bracketPoint(1629, X)
    
    return 35.53 - 0.56*NormY[A1657, :] + 0.60*NormY[A1629,:]
