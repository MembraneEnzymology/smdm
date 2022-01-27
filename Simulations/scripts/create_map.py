#!/usr/bin/env python
# coding: utf-8

# Periodic boundaries with surfaces
import numpy as np
import pandas as pd

def critical_points_cell(center, radius, length):
    
    cx = center[0]
    cy = center[1]
    cz = center[2]
    lx = - length/2 + cx
    clx = - length/2 + radius + cx
    crx = length/2 - radius + cx
    rx = length/2 + cx
    top = radius + cy
    bot = - radius + cy
    pos = radius + cz
    neg = radius - cz
    
    return cx, cy, cz, lx, clx, crx, rx, top, bot, pos, neg

def create_map(center, radius, length, array, map_res, delta_t, time_step, D, N, path):
    
    # rows to skip are given by delta_t/time_step
    jump = int(delta_t/time_step)
    
    x_elements = array[:, 1::3].copy()
    y_elements = array[:, 2::3].copy()
    
    cx, cy, cz, lx, clx, crx, rx, top, bot, pos, neg = critical_points_cell(center, radius, length)
    
    # define number of pixels in x and y axes
    x_pixels = int((rx - lx)/map_res)
    y_pixels = int((top - bot)/map_res)
    
    # define bin edges in x and y axes
    x_bins = np.array([lx + i*map_res for i in range(x_pixels + 1)])
    y_bins = np.array([bot + i*map_res for i in range(y_pixels + 1)])

    # identify which x_elements fall between which bins and return the indices of the x_elements in the order of the bins
    # AKA Return the indices of the bins to which each value in input array belongs.
    x_indices = np.digitize(x_elements, x_bins) - 1
    y_indices = np.digitize(y_elements, y_bins) - 1
    
    # create empty dataframe with y_pixel rows and x_pixel columns
    df = pd.DataFrame(data = [], index = range(y_pixels), columns = range(x_pixels))

    # substitute nan with empty list to append values
    df = df.applymap(lambda x: [])

    # iterate through each row of the database
    for i in range(len(x_indices) - jump):
        
        # iterate through each column of the database
        for j in range(len(x_indices[0])):
            
            df.iat[y_indices[i][j], x_indices[i][j]].append(([x_elements[i][j], y_elements[i][j], x_elements[i + jump][j], y_elements[i + jump][j]]))
            
    # define file name
    fname = 'billiard_cx_' + str(cx) + '_cy_' + str(cy) + '_len_' + str(rx-lx) + '_diam_' + str(top-bot) + '_D_' + str(D) + '_N_' + str(N) + '_map_df.csv.zip'
    fpath = path + '\\billiard_cx_' + str(cx) + '_cy_' + str(cy) + '_len_' + str(rx-lx) + '_diam_' + str(top-bot) + '_D_' + str(D) + '_N_' + str(N) + '_map_df.csv.zip'
        
    return df, fpath, fname


def save_df(df, fpath, fname):
    
    df.to_csv(fpath)
    
    return fname

