def nIntegrate(x0, x1, X, Y):
    '''
    Integrates the function generated by linearly interpolating the data X, Y 
    between x0 and x1.

    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        x0: starting wavelength of interest
        x1: end wavelength of interest
        
    Output:
        Vector containing calculated area of interest for each spectra
        
    '''
    from photizo.preprocessing.bracketPoint import bracketPoint
    from photizo.preprocessing.linearInterpolate import linearInterpolate
    from photizo.quantification.nIntegrateSimple import nIntegrateSimple
    from photizo.quantification.trapezium import trapezium
    
    #Central area
    i0 = bracketPoint(x0, X)
    i1 = bracketPoint(x1, X)
    
    interior_area = nIntegrateSimple(i0+1, i1, X, Y)
    
    #Remaining area on the left and right
    yL = linearInterpolate(X[i0:i0+2], Y[i0:i0+2], x0)
    yR = linearInterpolate(X[i1:i1+2], Y[i1:i1+2], x1)

    left = trapezium([x0, X[i0+1]], [yL, Y[i0+1]])
    right = trapezium([X[i1], x1], [Y[i1], yR])
    
    return left+interior_area+right
