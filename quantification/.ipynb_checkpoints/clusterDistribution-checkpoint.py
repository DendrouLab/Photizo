def clusterDistribution(adata, name, leiden):
    '''
    Inputs:
        adata: anndata object with spectra in adata.X and metadata in adata.obs
        name: column in adata.obs containing sample names
        leiden: column in adata.obs containing cluster classification of interest
    Output:
        Stacked barplot visualisation of cluster distribution across samples
    Note:
        to adjust position of legend, alter bbox coordinates
    '''
    import scanpy as sc
    import pandas as pd
    tmp = pd.crosstab(adata.obs[name],adata.obs[leiden],normalize='index')
    tmp.plot.bar(stacked=True).legend(bbox_to_anchor=(1.0, 1.0))
    plt.show()
