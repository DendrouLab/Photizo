def PCAprojection(m, n, fit, EVR):
    '''
    Inputs:
        m: First principal component of interest
        n: Second principal component of interest
        fit: matrix containing fitted data
        EVR: list containing all explained variance ratios
        
    Output:
        Graph plotting PCm vs PCn
    Note:
        To colour points based on metadata, modify the plt.scatter line to include c=list_of_metadata_values and cmap=colourmap_of_choice
    '''

    import matplotlib.pyplot as plt
    import matplotlib
    import pylab as pl

    plt.figure()
    plt.scatter(fit[:, m-1], fit[:, n-1], s=4, lw=0, alpha = 0.5)
    cbar = pl.colorbar(ticks = (0, 1))
    #cbar.ax.set_yticklabels(['Category_1', 'Category_2']) 
    plt.xlabel('PC%i (%s%% EVR)' % (m, int(100*EVR[0])))
    plt.ylabel('PC%i (%s%% EVR)' % (n, int(100*EVR[1])))
    #pl.xlim([-0.015, 0.015])
    #pl.ylim([-0.01, 0.018])
    plt.title('PCA projection')
    plt.savefig('PCA_PC%i_PC%i_projection.png' % (m,n), dpi = 300)
    plt.show()