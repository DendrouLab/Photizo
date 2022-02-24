def PCA(wavelengths, Y):
    '''
    Description: This is a function for PCA which shows a plot of the cumulative explained variance ratio (elbow plot) and the top 3 eigenspectra. 
    It returns the pca result, which can then be used for specific plotting e.g.: for top PC projection scatter plots. 
    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix without excluded spectra
        n: number of principal components
    Output:
        Shows Cumulative explained variance
        Shows top 3 eigen-spectra
        Returns PCA explained variance ratio, pca components and data after fit transformation
    Note: 
        Performing PCA on spectroscopic data can benefit from taking as input the second derivative of spectra, since this controls for the baseline. 
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    import pylab as pl
    from sklearn.decomposition import PCA 
    import pandas as pd

    pca = PCA().fit(Y)        
    fit = pca.fit_transform(Y)
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')
    plt.savefig('PCA_CEV.png', dpi = 300)
    plt.show()

    pl.figure()                                                          
    for i in range(3):
        l = pl.plot(wavelengths, pca.components_[i] + 0.40 * i)
        c = l[0].get_color()
        pl.text(3200, -0.01 + 0.40 * i, "component %i" % (i + 1), color='#00188B')
    plt.xlabel('Wavenumber')
    plt.ylabel('Absorbance + offset')
    plt.title('Eigen-spectra')
    plt.savefig('PCA_eigenspectra.png', dpi = 300)
    plt.show()
    
    return pca.explained_variance_ratio_, pca.components_, fit