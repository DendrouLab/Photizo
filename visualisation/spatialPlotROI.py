def spatialPlotROI(X, Y0VNH, a, b, x0, x1, title):
    '''
    This function is for visualising the semi-quantitative integrated values spatially in a sample.
    We recommend this function be used for inspection of spectral exclusion. 

    Inputs:
        X: Vector with ordered wavelengths
        Y: Ordered matrix with excluded spectra reinserted as 0.0
        x0: Lower limit of region of interest
        x1: Upper limit of region of interest
        a: number of pixels in the X (horizontal) axis
        b: number of pixels in the Y (vertical) axis
        title: plot title
        
    Output:
        Vector containing calculated area of interest for each spectra controlling for the spectral baseline
        
    '''
    import matplotlib.pyplot as plt
    import photizo.quantification as pzq
    integrated = pzq.adjustedIntegrate(x0, x1, X, Y0VNH)
    integrated = integrated.reshape(b,a)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.imshow(integrated, extent = [0, a, 0,b], cmap = 'jet')
    plt.colorbar()
    plt.title('%s' % title)
    plt.savefig('%s_spectra_ROI_plot.png' % title, dpi = 300)
    plt.show()