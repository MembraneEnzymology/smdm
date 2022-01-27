# Protein Diffusion in Escherichia coli cytoplasm using Single-Molecule Displacement Mapping (SMdM) #

This is a repository of code developed in the Membrane Enzymology group of University of Groningen for the analysis of protein diffusion in Escherichia coli cytoplasm using Single-Molecule Displacement Mapping (SMdM).

## Bioinformatic analysis ##
* 01 - Creating SQL from IntAct : This notebook is used to import data from the IntAct database into our own Postgres database
* 02 - Importing abundance data : This notebook imports data from the Schmidt et al. 2015 database into postgreSQL database and merges it with the IntAct database
* 03 - Queries and picking POIs : Counting interactions, checking GeneOntology, detailed statistics per unique interaction, exports, processing with pandas, plotting, comments, markdown, conversion to notebook
* data.zip : this file contains the data that we used in our analysis

## Microscopy ##
* Analysis_script_all_features
* Analysis script : performs SMdM and analysis the measurements
* Concatenate and find peaks : concatenates measurements into one tiff file that can be used by the analysis script
* Laser modulation : modulates the lasers in our measurement setup

## Notebook for figures and data analysis ##

## Simulations ##

## Simulations data for supplementary ##

## Used Python packages ##
* [numpy] (http://www.numpy.org/)
* [pandas] (https://pandas.pydata.org/)
* [matplotlib] (http://matplotlib.org/)
* [scipy] (https://www.scipy.org/)
* [h5py] (https://www.h5py.org/)
* [tifffile] (https://pypi.org/project/tifffile/)
* [storm_analysis] (https://github.com/ZhuangLab/storm-analysis)
* [psycopg2] (https://pypi.org/project/psycopg2/)
* [PyDAQmx] (https://pypi.org/project/PyDAQmx/)
