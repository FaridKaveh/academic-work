#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:01:52 2019

@author: farid
"""

from matplotlib import pyplot as plt 
import matplotlib.gridspec as gridspec
import pickle 
import numpy as np


infile = open("fitsVar", "rb")
infile_1 = open('5x5data', 'rb')
infile_2 = open('10x10data', 'rb')
infile_3 = open('50x50data', 'rb')
infile_4 = open('100x100data', 'rb')

data_5  = pickle.load(infile_1)
data_10 = pickle.load(infile_2)
data_50 = pickle.load(infile_3)
data_100 = pickle.load(infile_4)
to_plot = pickle.load(infile)

infile_1.close()
infile_2.close()
infile_3.close()
infile_4.close()
infile.close()

for data in to_plot:
    for key in data: 
        print(key, data[key]['variances'])


#plt.loglog(data_100["Topples"][0], np.exp(to_plot[3]["Topples"]["fit"]))
#plt.plot(data_100["Topples"][0],data_100["Topples"][1])
#plt.show()



