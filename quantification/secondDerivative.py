def secondDerivative(X, Y, order):
    '''
    Inputs:
        X: a vector with wavelengths
        Y: a matrix with all spectra
        order: polynomial order for second derivative  
    Output:
        plot of mean second derivative spectrum with standard deviation
        dY: matrix with second derivative of all spectra
    '''
    from scipy.signal import savgol_filter
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    import pylab as pl
    from sklearn.decomposition import PCA
    
    dY = savgol_filter(Y, 11, polyorder = order, deriv = 2)       #Calculation of numerical second derivative of spectra using a Savitzky-Golay filter for smoothing 
    mu = np.array(dY.mean(0))                                            #Plot mean spectra in black with standard deviation in grey
    std = dY.std(0)
    plt.plot(X, mu, color='black')
    plt.fill_between(X, mu - std, mu + std, color='#8D94B4')
    plt.xlim(X[0], X[-1])
    plt.xlabel('Wavenumber')
    plt.ylabel('Absorbance')
    plt.title('Mean Spectrum')
    plt.show()
    return dY.T