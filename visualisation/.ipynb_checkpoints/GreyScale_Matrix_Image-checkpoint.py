def GreyScale_Matrix_Image(sqrsx, sqrsy, GreyScale):
    count=0
    
    mat = np.zeros(shape=(sqrsy,sqrsx))
    for m in range (0,sqrsy):
        for n in range (0,sqrsx):
            mat[m,n]=GreyScale[count]
            count+=1
    return mat