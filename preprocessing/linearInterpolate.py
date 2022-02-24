def linearInterpolate(xs, ys, x):
    return ys[0] + (x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
