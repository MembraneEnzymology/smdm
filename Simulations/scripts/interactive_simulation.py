#!/usr/bin/env python
# coding: utf-8

import os
import time
import numpy as np
import matplotlib.pyplot as plt
from . import smoldyn_simulation as sms
from . import create_map as cmap  # if you want only map of the three regions (poles and center) change create_map with create_map_three_zones
from . import diffusion_fit_first as fdiff

def sim_map_fit(radius, length, D, map_res, delta_t, p0, disp_SMDM_minimum):
    
    seed = int(time.time())
    path = os.getcwd()
    path += '\\files\\maps 1 5 10'  # change path name to where you want to have files saved
    
    # values for smoldyn
    center = [0,0,0]  # center of the cell
    N = 500  # number of particles
    total_time = 2  # simulation time
    time_step = 0.0001  # time steps

    # create simulation
    simulation_file, sim_file_path, sim_file_name = sms.smoldyn_billiard(center, radius, length, N, D, total_time, time_step, seed, path)
    sms.save_data(simulation_file, sim_file_path)
    
    # create displacements map
    simulation_map, sim_map_path, sim_map_name = cmap.create_map(center, radius, length, simulation_file, map_res, delta_t, time_step, D, N, path)
    map_name = cmap.save_df(simulation_map, sim_map_path, sim_map_name)
    
    # create diffusion map
    diffusion_map, diffusion_average = fdiff.create_map_fit(simulation_map, delta_t, p0, disp_SMDM_minimum)
    diff_map_name = fdiff.save_map_fit(diffusion_map, sim_map_path, sim_map_name)
    
    # plot diffusion map
    plt_name = diff_map_name[:-8] + '.png'
    plt_path = path + '\\' + plt_name
    map0 = fdiff.draw_map(diffusion_map, diffusion_average)
    plt.savefig(plt_path, dpi = 300, format = 'png')
    plt.close('all')
    
    return diffusion_map

def routine():
    
    # generate a set of radi and length randomly distributed between a minimum and a maximum
    min_width = input('input min width: ')
    max_width = input('input max width: ')
    
    min_width = float(min_width)
    max_width = float(max_width)
    
    radi = np.random.uniform(min_width/2, max_width/2, 5)
    
    min_length = input('input min length: ')
    max_length = input('input max length: ')
    
    min_length = float(min_length)
    max_length = float(max_length)
    
    lengths = np.random.uniform(min_length/2, max_length/2, 5)
        
    Diffs = []
    print('input 5 values for D in um^2/s, 1 per time')
    for i in range(5):
        
        D = input('> ')
        D = float(D)
        Diffs.append(D)
        
    # create all possible combinations of radi, lengths, diffusions    
    RLD = np.meshgrid(radi, lengths, Diffs, indexing = 'ij')
    RLD = np.array(RLD).T
    RLD = np.vstack(np.vstack(RLD))
    
    # if diameter >= length, remove the entry
    index = np.where(RLD[:,0]*2 < RLD[:,1])[0]
    RLD = RLD[index]
    
    delta_t = input('input delta_t for displacements in seconds: ')
    delta_t = float(delta_t)
    
    p0 = input('input first guess for diffusion simulation: ')
    p0 = float(p0)
    
    disp_SMDM_minimum = input('input value for minimum number of displacements per pixel: ')
    disp_SMDM_minimum = float(disp_SMDM_minimum)    
    
    map_res = input('input value for map resolution: ')
    map_res = float(map_res)   
    
    print('starting the simulation, map and fitting for all possible combinations of radi, lengths and D..')
    
    for element in RLD:

        print('using the following combination:', element)

        diffusion_map = sim_map_fit(*element, map_res, delta_t, p0, disp_SMDM_minimum)
    
    print('routine finished.')
    
    return diffusion_map
