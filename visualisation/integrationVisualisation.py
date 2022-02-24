def integrationVisualisation(Y, X, title, x0, x1):
    '''
    This function is for visualising the mean spectrum of a given sample with the corresponding standard deviation. 
    By inserting values of a region of interest in x0 and x1, one can visually inspect the integration window in relation to the spectrum prior to quantitative analysis. 

    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix without excluded spectra
        title: Plot title
        x0: Lower limit of region of interest
        x1: Upper limit of region of interest
        
    Output:
        Vector containing calculated area of interest for each spectra controlling for the spectral baseline
        
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    plt.axes()
    plt.plot(X, Y.mean(1), color = 'teal')  
    mu = np.array(Y.mean(1))
    std = Y.std(1)
    plt.fill_between(X, mu - std, mu + std, color='#CCCCCC')   
    plt.fill_between(X, 0, 0.2, where=(X>x0) & (X<x1),
                color='slategrey', alpha=0.5)
    plt.axis([900, 3100, -0.006, 0.2])
    plt.title('%s' % title, loc='center', size=14)
    plt.xlabel('Wavenumber', size=12)
    plt.ylabel('Absorbance', size=12)
    plt.savefig('%s_integration_map.png' % title, dpi = 300)
    plt.show()