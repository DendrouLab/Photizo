def random(X,Y):
    '''
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        
    Output:
        % contribution of random folding based on method described by Goormaghtigh et al, 2009
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    from photizo.quantification.nIntegrate import nIntegrate
    NormY = (Y/Area)*10000
    A1523 = bracketPoint(1523, X)
    A1679 = bracketPoint(1679, X)
    
    return -40.65 + 1.08 * NormY[A1523, :] + 0.62 * NormY[A1679, :]
