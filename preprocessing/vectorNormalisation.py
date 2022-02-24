def vectorNormalisation(Y):
    import numpy as np
    return Y / np.linalg.norm(Y, axis=0)