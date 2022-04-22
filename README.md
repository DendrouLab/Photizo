# Photizo v. 0.001
Photizo is a python-based library for analysis of spectral data. It has been optimised for analysis of infrared scanning spectroscopy and infrared imaging with focal plane array detector, but has flexible functionality and may be adaptable for analysis of other spectral data. The expected spectral data should be in a txt format with the first column containing wavenumbers and each subsequent column containing data for a single spectrum (default format exported from OPUS 7.4 in dpt format). Prior to exporting from OPUS, we recommend Cutting the spectrum to exclude noisy areas, applying atmospheric compensation and baseline correction. Please note that to make use of spatially resolved visualisation the user must have the number of spectra collected in the X and Y axis. 

Photizo was written in Python 3.7.4 with the following package versions: 

pandas==1.1.3;
numpy==1.19.2;
matplotlib==3.3.2;
astropy==4.0.3;
scikit-image==0.17.2;
scikit-learn==0.23.2;
scipy==1.5.3;
umap==0.1.1;
scanpy==1.6.0;
leidenalg==0.8.2;
anndata==0.7.4

We have made available on Zenodo raw spectral data collected from IR imaging with FPA detector from biological specimens (https://zenodo.org/record/6417982#.Yk2O9TfMI6A), this data is intended to be used with an example workflow written in jupyter notebooks. Detailed information about functionality is available in the documentation. 

This library has been tested with datasets with up to ~300,000 spectra from 19 samples.
