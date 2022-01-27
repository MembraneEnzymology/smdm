# Protein Diffusion in Escherichia coli cytoplasm using Single-Molecule Displacement Mapping (SMdM) #

This is a repository of code developed in the Membrane Enzymology group of University of Groningen for the analysis of protein diffusion in Escherichia coli cytoplasm using Single-Molecule Displacement Mapping (SMdM).

The repository is organized into three parts :
1. The bioinformatic analysis part is used to find protein candidates for diffusion measurements
2. The microscopy part contains all the notebooks for microscopy data acquisition and analysis
3. The simumlation part contains all the code for performing diffusion simulations with Smoldyn (https://www.smoldyn.org) and for simulation data analysis
4. The figures and data analysis part contains the notebook that was used to generate the figures and to perform the statistical analysis in our paper using the excel spreadsheets that are present in that folder

## Bioinformatic analysis ##
* 01 - Creating SQL from IntAct.ipynb : This notebook is used to import data from the IntAct database into our own Postgres database
* 02 - Importing abundance data.ipynb : This notebook imports data from the Schmidt et al. 2016 database into postgreSQL database and merges it with the IntAct database
* 03 - Queries and picking POIs.ipynb : Counting interactions, checking GeneOntology, detailed statistics per unique interaction, exports, processing with pandas, plotting, comments, markdown, conversion to notebook
* data.zip : this file contains the data that we used in our analysis

## Microscopy ##
* Laser modulation.ipynb : modulates the lasers in our measurement setup
* Concatenate and find peaks.ipynb : concatenates measurements into one tiff file that can be used by the analysis script
* Parameters.xml : this file contains all the settings used for peak finding using the Storm Analysis package (https://github.com/ZhuangLab/storm-analysis)
* Analysis script.ipynb : performs SMdM and analysis the measurements

## Simulations ##
* run_sim_map_fit.py: starts the program for running the simulation, using the module interactive_simulation included in the package "scripts"
* scripts
	* interactive_simulation.py: receives input from user to define a set of radi, lengths and diffusion coefficients to run different simulations. Inside this file the users can specify the path in which they want to save the output files
	* smoldyn_simulation.py: starts the diffusion simulation using the package "smoldyn"
	* create_map.py: creates a map of displacements using the desired pixel size
	* create_map_three_zones.py: divides the cell in three zone (cell center and cell poles) and create a map of displacements
	* diffusion_fit_first.py: performe a fit of the displacements to obtain the diffusion coefficient

## Notebook for figures and data analysis ##
Once the simulations have been performed, the folders containing the output data need to be moved in this folder to perform data analysis and to create the figures.
* figures_and_analysis.ipynb: creates figures and analyze data by loading the files obtained from simulations (paths need to be change accordingly inside the notebook) and by loading the spreadsheets containing the information about diffusion coefficients and cell sizes located in the folder. The data reported in these spreadsheets were obtained through microscopy measurements and are the ones used in our paper.

## Used Python packages ##
* [numpy] (http://www.numpy.org/)
* [pandas] (https://pandas.pydata.org/)
* [matplotlib] (http://matplotlib.org/)
* [seaborn] (https://seaborn.pydata.org/)
* [scipy] (https://www.scipy.org/)
* [h5py] (https://www.h5py.org/)
* [tifffile] (https://pypi.org/project/tifffile/)
* [storm_analysis] (https://github.com/ZhuangLab/storm-analysis)
* [smoldyn] (https://github.com/ssandrews/Smoldyn)
* [psycopg2] (https://pypi.org/project/psycopg2/)
* [PyDAQmx] (https://pypi.org/project/PyDAQmx/)


