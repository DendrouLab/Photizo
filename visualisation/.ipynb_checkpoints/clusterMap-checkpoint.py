def clusterMap(sqrsy, sqrsx, Y0, name):
    '''
    This function is optimised to map uFTIR data with known dimensions of pixels/spectra. The user may modify the input RGB code for each cluster as needed, with example values given here:
    
    Turquoise = (0.4, 0.76078431, 0.64705882)
    Orange = (0.98823529, 0.55294118, 0.38431373)
    Pink = (0.90588235, 0.54117647, 0.76470588)
    Green = (0.65098039, 0.84705882, 0.32941176)
    Purple = (0.60, 0.48, 0.8)
    Blue = (0.55294118, 0.62745098, 0.79607843)
    Tan = (0.89803922,0.76862745, 0.58039216)
    Yellow = (1., 0.85098039, 0.18431373)
    Grey = (0.55294118, 0.55294118, 0.55294118)
    Black = (0, 0, 0)
    
    Inputs:
        sqrsx: Number of pixels in the X axis
        sqrsy: Number of pixels in the Y axis
        Y0: Vector containing cluster classification of all pixels. This vector must have a value of -99 inserted in the positions where spectra were excluded.
        
    Output:
        returns image of mapped cluster classification
    '''
    from photizo.preprocessing.makeRGB import makeRGB
    from photizo.preprocessing.matrixImage import matrixImage
    import matplotlib.pyplot as plt
    import numpy as np
    
    
    Y_mtx = Y0.reshape((sqrsx, sqrsy))
    dim_Y = np.shape(Y_mtx)
    red=np.zeros(shape=(dim_Y[0], dim_Y[1]))
    green=np.zeros(shape=(dim_Y[0], dim_Y[1]))
    blue=np.zeros(shape=(dim_Y[0], dim_Y[1]))

    a = 0
    b = 0
    for a in range (0, dim_Y[1]-1):
        for b in range (0, dim_Y[0]-1):
            if Y_mtx[b, a]==0:
                red[b,a]=0.4            #Turquoise
                green[b,a]=0.76078431
                blue[b,a]=0.64705882
            if Y_mtx[b, a]==1:        #Orange
                red[b,a]=0.98823529
                green[b,a]=0.55294118
                blue[b,a]=0.38431373
            if Y_mtx[b, a]==5:        #Pink
                red[b,a]=0.90588235
                green[b,a]=0.54117647
                blue[b,a]=0.76470588
            if Y_mtx[b, a]==3:        #Green
                red[b,a]=0.65098039
                green[b,a]=0.84705882
                blue[b,a]=0.32941176
            if Y_mtx[b, a]==2:        #Blue
                red[b,a]=0.55294118
                green[b,a]=0.62745098
                blue[b,a]=0.79607843
            if Y_mtx[b, a]==7:        #Tan
                red[b,a]=0.89803922
                green[b,a]=0.76862745
                blue[b,a]=0.58039216
            if Y_mtx[b, a]==4:        #Yellow
                red[b,a]=1.
                green[b,a]=0.85098039
                blue[b,a]=0.18431373
            if Y_mtx[b, a]==-99 or Y_mtx[b, a]==-1:        #Grey
                red[b,a]=0.95
                green[b,a]=0.95
                blue[b,a]=0.95
            if Y_mtx[b, a]==6:        #Purple
                red[b,a]=0.60
                green[b,a]=0.48
                blue[b,a]=0.8

    plt.imshow(makeRGB(red, green, blue))
    plt.savefig('%s_cluster_map.png' % name, dpi = 300)
    plt.show()
