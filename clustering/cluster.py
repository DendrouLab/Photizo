def cluster(adata, n_neigh = 15, spread = 1.0, min_dist = 0.1, leiden_res = 0.1):
    '''
    Inputs:
        adata: adata object with spectral information in adata.X and spectral annotation in adata.obs
        n_neigh: number of neighbours for subsequent UMAP calculation. Default: 15
        spread: spread value for UMAP. Default: 1.0
        min_dist: minimum distance for UMAP. Default: 0.1
        leiden_res: leiden resolution for community detection. Default: 0.1
        
    Output:
        adata object with new UMAP and leiden variables. 
    '''
    import scanpy as sc
    
    sc.pp.neighbors(adata, n_neighbors=n_neigh, use_rep='X')
    sc.tl.umap(adata, spread = spread, min_dist = min_dist)
    sc.tl.leiden(adata, key_added = 'leiden', resolution = leiden_res)
    
    return adata