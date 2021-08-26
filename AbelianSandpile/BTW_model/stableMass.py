#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:33:03 2019

@author: farid
"""

import pathlib
import numpy as np
import matplotlib.ticker as mtick
#import numpy as np
from sandpile import SandPile
from system import system_timed, system_stable, first_avalanche_dist, stable_avalanches
from matplotlib import pyplot as plt
#from cycler import cycler
import pickle
from cycler import cycler

#outfile1 = open("mass_hist5","wb")
#outfile2 = open("mass_hist10","wb")
#outfile3 = open("mass_hist50","wb")
#outfile4 = open("mass_hist100","wb")
#
#data_5 = system_timed(5,5,50000)
#data_10 = system_timed(10,10,50000)
#data_50 = system_timed(50,50,50000)
#data_100 = system_timed(100,100,50000)
#
#pickle.dump(data_5, outfile1)
#pickle.dump(data_10, outfile2)
#pickle.dump(data_50, outfile3)
#pickle.dump(data_100, outfile4)
#
#outfile1.close()
#outfile2.close()
#outfile3.close()
#outfile4.close()

outfile1 = open("mass_hist5","rb")
outfile2 = open("mass_hist10","rb")
outfile3 = open("mass_hist50","rb")
outfile4 = open("mass_hist100","rb")

data_5 = np.array(pickle.load(outfile1))
data_10 = np.array(pickle.load(outfile2))
data_50 = np.array(pickle.load(outfile3))
data_100 = np.array(pickle.load(outfile4))

to_plot = [data_5,data_10,data_50,data_100]

plt.rcParams.update({'font.size': 22})
plt.rcParams["font.sans-serif"] = "Helvetica"
plt.rcParams["font.family"] = "serif"

fig, ax = plt.subplots()


ax.set_prop_cycle(cycler('color', ['forestgreen', 'darkmagenta', 'black', 'darkorange']))

ax.set(ylabel = "Average site mass", xlabel = "Time step")

#ax.plot(data_5/25, alpha = 1, label = "5x5 grid")

ax.plot(data_10/100, alpha = 1, label = "10x10 grid")
#ax.plot(data_50/2500, label = "50x50 grid")
#ax.plot(data_100/10000, label = "100x100 grid")
    
#
#axs[0,0].set(title = "5x5 grid")
#axs[0,1].set(title = "10x10 grid")
#axs[1,0].set(title = "50x50 grid")
#axs[1,1].set(title = "100x100 grid")
#ax.set_xscale('log')
ax.legend(loc = "best")
ax.set_xlim(2e4,2.1e4)

#ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#axs[1,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))

#for ax in axs.flat: 
#    ax.legend(loc = 'best')

#fig.subplots_adjust(hspace = 0.35)
#print(len(data_50)-len(data_50[-1000:-1]),len(data_100)- len(data_100[-2000:-1]))
plt.show()



