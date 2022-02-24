def holeExclusion(i, j, X, Y):
    '''
    Inputs:
        X: a vector with wavelengths
        Y: a matrix with all spectra
        
    Output:
        returns Y_zeros - matrix with spectra from holes or with scattered light converted to zero
                Y_nozeros - matrix without spectra from holes or with scattered light
                idx - indexes of positions of excluded spectra
                
    We recommend visualising Y_zeros spatially to confirm that excluded spectra overlapp with holes or regions with damaged sample
    '''
    
    from photizo.preprocessing.selectRegionY import selectRegionY
    import numpy as np

    Y_zeros = np.copy(Y)
    Y_nozeros = np.zeros(shape=(i,j))
    Lipid_Peaks=selectRegionY(2800, 3000, X,Y)
    Protein_Peaks=selectRegionY(1500, 1700, X,Y)
    Baseline_Delta=selectRegionY(1900, 2700, X, Y)

    for x in range (0,j-1):
        if Lipid_Peaks[:,x].max()<(Lipid_Peaks.max())/4 and Protein_Peaks[:,x].max()<(Protein_Peaks.max())/4:
            Y_zeros[:,x]=0
        elif (((Baseline_Delta[:,x].max()))-(Baseline_Delta[:,x].min()))>((np.average(Baseline_Delta, axis=1).max())-(np.average(Baseline_Delta, axis=1).min()))*5:
            Y_zeros[:,x]=0
        elif np.mean(Baseline_Delta[:,x])>np.mean(np.average(Baseline_Delta, axis=1))*5:
            Y_zeros[:,x]=0

    idx = np.argwhere(np.all(Y_zeros == 0, axis=0))
    n=idx
    Y_nozeros = np.delete(Y_zeros, n, axis=1)
    
    return Y_zeros, Y_nozeros, idx
