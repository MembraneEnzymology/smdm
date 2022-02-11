#!/usr/bin/env python
# coding: utf-8

# Periodic boundaries with surfaces
import numpy as np
import pandas as pd
import smoldyn

# save the time and feed it as random seed to smoldyn to output the graphics and then run the code for data --> done
# find a way to restart program after it stops due to openGL
# convert output into pandas dataframe

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
    neg = - radius + cz
    
    return cx, cy, cz, lx, clx, crx, rx, top, bot, pos, neg

def smoldyn_billiard(center, radius, length, N, D, total_time, time_step, seed, path):
    
    # get shape limits
    cx, cy, cz, lx, clx, crx, rx, top, bot, pos, neg = critical_points_cell(center, radius, length)

    # set limits of axes
    left_axis = lx - 0.5
    right_axis = rx + 0.5
    bot_axis = bot - 0.5
    top_axis = top + 0.5
    neg_axis = neg - 0.5
    pos_axis = pos + 0.5
    
    # define length of the horizontal part of the billiard
    horizontal_size = [crx - clx]

    # create simulation environment defining the bottom left corner and the top right
    s = smoldyn.Simulation(low = [left_axis, bot_axis, neg_axis], high = [right_axis, top_axis, pos_axis], seed = seed)

    # add a molecular specie with a diffusion coefficient D
    A = s.addSpecies("A", difc = D, color = "green")

    # create the different parts of the billiard
    s_right = smoldyn.Hemisphere(center = [crx, cy, cz], radius = radius, vector = [-1 ,0, 0], slices = 1000, stacks = 1000, name = 's_right')
    s_left = smoldyn.Hemisphere(center = [clx, cy, cz], radius = radius, vector = [1, 0, 0], slices = 1000, stacks = 1000, name = 's_left')
    s_center = smoldyn.Cylinder(start = [clx, cy, cz], end = [crx, cy, cz], radius = radius, slices = 1000, stacks = 1000, name = 's_center')

    # create the billiard by merging together the different parts
    billiard = s.addSurface("billiard", panels=[s_left, s_center, s_right])

    # define action of reflection for the billiard walls
    billiard.setAction('both', [A], "reflect")
    billiard.setStyle('both', color = 'white', thickness = 1.0)

    # create a compartment inside the billiard and place N molecules randomly in the compartment
    cell = s.addCompartment('cell', surface = billiard, point = [cx, cy, cz])
    cell.simulation.addCompartmentMolecules('A', N, 'cell')
    
    # define file name
    fname = 'billiard_cx_' + str(cx) + '_cy_' + str(cy) + '_len_' + str(rx-lx) + '_diam_' + str(top-bot) + '_D_' + str(D) + '_N_' + str(N) + '.npz'
    fpath = path + '\\billiard_cx_' + str(cx) + '_cy_' + str(cy) + '_len_' + str(rx-lx) + '_diam_' + str(top-bot) + '_D_' + str(D) + '_N_' + str(N) + '.npz'
    
    # add info about the molecules position at eacht time step in an output to return at the end of the function (so it's not necessary to read the file every time)
    s.addOutputData('mydata')
    s.addCommand(cmd = "molpos A mydata", cmd_type = "E")

    # run the simulation
    s.run(total_time, dt = time_step, overwrite = True)
    
    # retrieve output data after running the simulation
    data = s.getOutputData('mydata', 0)
    
    # convert output in numpy array
    data = np.array(data)
    
    return data, fpath, fname

def save_data(data, fpath):
    
    np.savez_compressed(fpath, data = data)
    
    return
