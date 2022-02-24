def bracketPoint(x, X):
    '''
    Inputs:
        X: a vector of numbers ordered from smallest to largest
        x: a real valued number
        
    Output:
        returns the index i such that X[i]<x<X[i+1]
    '''
    
    if x<X[0] or x>X[-1]:
        raise ValueError('The point x is outside the suitable range of values')
        
    i = 0
    while x>X[i+1]:
        i+=1
        
    return i