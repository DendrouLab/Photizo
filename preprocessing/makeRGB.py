def makeRGB(red, green, blue):
    '''
    Inputs:
        Three matrices of the same size, each of which correponds to the R, G or B value of a given pixel
        
    Output:
        Image corresponding to the merged RGB matrices
    '''
    from astropy.visualization import make_lupton_rgb
    
    return make_lupton_rgb(red, green, blue, stretch=0.5)     #Approach described by Lupton et al 2004
