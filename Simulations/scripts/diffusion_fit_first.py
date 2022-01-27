#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
from matplotlib import pyplot as plt


def diff_func(dists, t, D):
    
    k = 4*D*t
    num = np.exp(-(dists**2)/(k))
    
    return (2*dists*num)/k


def final_fitting_function(x, t, p0, disp_SMDM_minimum):
    
    if p0 <= 0:
        
        print('Diffusion coefficient cannot be <= 0')
        return

    # if there are not enough data in the cell, don't start the fitting routine
    if len(x) <= disp_SMDM_minimum:
        return 0
    
    else:
        
        # transpose the data in the cell to have all the x in first row, all the y in second etc
        x = np.array(x).transpose()
        
        # assign the data to variables
        x0 = x[0]
        y0 = x[1]
        x1 = x[2]
        y1 = x[3]
        
        # calculate squared distance
        dists = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        
        # pack distance and time
        xy = [dists, t]
        
        def find_log(D, xy):
    
            # unpack values
            dists, t = xy
        
            # calculate logarithm and return sum of log --> less expensive than calculating the function and computing the multiplication
            my_log = np.log(diff_func(dists, t, D))

            return -np.sum(my_log)
        
        # apply the minimize method
        result = minimize(find_log, p0, xy, method = 'Nelder-Mead')
        
        #return the first and only element of the array x stored in result
        return result.x[0]
    
# create map of fitted values
def create_map_fit(df, t, p0, disp_SMDM_minimum):
    
    df = df.applymap(lambda x: final_fitting_function(x, t, p0, disp_SMDM_minimum))
    map_fit_array = df.to_numpy()
    map_fit_array = map_fit_array.ravel()
    
    indexes = np.where(map_fit_array == 0)[0]
    map_fit_array = np.delete(map_fit_array, indexes)
    
    average = np.mean(map_fit_array)
    
    return df, average

# save map fit
def save_map_fit(map_fit, fpath, fname):
    
    file_path = fpath[:-10] + 'diff_first_fit.csv.zip'
    file_name = fname[:-10] + 'diff_first_fit.csv.zip'
    
    map_fit.to_csv(file_path)
    
    return file_name

# draw the map
# when creating the map, the value vmax is to change accordingly to the data
def draw_map(map_fit, average):
    
    map0 = sns.heatmap(map_fit, cmap = 'PuOr_r', vmin = 0.5*average, vmax = 1.5*average, xticklabels = False, yticklabels = False, square = True)
    
    return map0

