def plotSpectra(Cluster_means, X, title):
    '''
    Plot mean spectra of each cluster
    
    Inputs:
        Cluster_means: matrix containing in each column the mean spectrum values of a given cluster
        X: vector containing wavelengths
        title: String containing title of plot
        
    Output:
        Returns graph plotting all mean spectra
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    ax = plt.axes()
    ax.set_prop_cycle('color',[plt.cm.Set2(d) for d in np.linspace(0, 1, np.shape(Cluster_means)[1])])
    for d in range(np.shape(Cluster_means)[1]):
        plt.plot(X, Cluster_means[:,d])
    plt.title('%s' % title, loc='center', size=14)
    plt.xlabel('Wavenumber', size=12)
    plt.ylabel('Absorbance', size=12)
    plt.savefig('%s_spectra_plot.png' % title, dpi = 300)
    plt.show()
