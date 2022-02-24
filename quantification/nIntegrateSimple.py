def nIntegrateSimple(i0, i1, X, Y):
    '''
    This function integrates the function which piecewise linearly interpolates the data X,Y.
    
    Note that the bounds of integration i0, and i1 refer to indexes, not
    numerical wavelength values.
    
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with all spectra
        i0: starting wavelength of interest
        i1: end wavelength of interest
        
    Output:
        Vector containing calculated area of interest for each spectra
        
    '''
    from photizo.quantification.trapezium import trapezium
    
    area = 0
    for i in range(i0, i1):
        area+= trapezium(X[i:i+2], Y[i:i+2])
    return area
