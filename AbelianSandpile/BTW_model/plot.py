import pathlib
import numpy as np
from matplotlib import pyplot as plt
from cycler import cycler
import pickle

""" Here I import the data and plot it. Polyfit was used for all the fits. """
infile = open("fits2", "rb")
infile_1 = open('5x5data', 'rb')
infile_2 = open('10x10data', 'rb')
infile_3 = open('50x50data', 'rb')
infile_4 = open('100x100data', 'rb')

data_5  = pickle.load(infile_1)
data_10 = pickle.load(infile_2)
data_50 = pickle.load(infile_3)
data_100 = pickle.load(infile_4)
fits = pickle.load(infile)

infile_1.close()
infile_2.close()
infile_3.close()
infile_4.close()
infile.close()

datas = [(data_5, '5x5 grid'),(data_10, '10x10 grid'),
           (data_50, '50x50 grid'),(data_100, '100x100 grid')]




log_x100_loss = np.log(data_100['Loss'][0][1:])
log_y100_loss = np.log(data_100['Loss'][1][1:])
log_x50_loss = np.log(data_50['Loss'][0][1:])
log_y50_loss = np.log(data_50['Loss'][1][1:])
log_x10_loss = np.log(data_10['Loss'][0][1:])
log_y10_loss = np.log(data_10['Loss'][1][1:])
log_x5_loss = np.log(data_5['Loss'][0][1:])
log_y5_loss = np.log(data_5['Loss'][1][1:])

log_x100_topples = np.log(data_100['Topples'][0][0:])
log_y100_topples = np.log(data_100['Topples'][1][0:])
log_x50_topples = np.log(data_50['Topples'][0][0:])
log_y50_topples = np.log(data_50['Topples'][1][0:])
log_x10_topples = np.log(data_10['Topples'][0][0:])
log_y10_topples = np.log(data_10['Topples'][1][0:])
log_x5_topples = np.log(data_5['Topples'][0][0:])
log_y5_topples = np.log(data_5['Topples'][1][0:])

log_x100_length = np.log(data_100['Length'][0][0:])
log_y100_length = np.log(data_100['Length'][1][0:])
log_x50_length = np.log(data_50['Length'][0][0:])
log_y50_length = np.log(data_50['Length'][1][0:])
log_x10_length = np.log(data_10['Length'][0][0:])
log_y10_length = np.log(data_10['Length'][1][0:])
log_x5_length = np.log(data_5['Length'][0][0:])
log_y5_length = np.log(data_5['Length'][1][0:])

log_x100_area = np.log(data_100['Area'][0][0:])
log_y100_area = np.log(data_100['Area'][1][0:])
log_x50_area = np.log(data_50['Area'][0][0:])
log_y50_area = np.log(data_50['Area'][1][0:])
log_x10_area = np.log(data_10['Area'][0][0:])
log_y10_area = np.log(data_10['Area'][1][0:])
log_x5_area = np.log(data_5['Area'][0][0:])
log_y5_area = np.log(data_5['Area'][1][0:])

areas_x = [log_x100_area, log_x50_area, log_x10_area, log_x5_area ]
areas_y = [log_y100_area, log_y50_area, log_y10_area, log_y5_area ]

losses_x = [log_x100_loss, log_x50_loss, log_x10_loss, log_x5_loss ]
losses_y = [log_y100_loss, log_y50_loss, log_y10_loss, log_y5_loss ]

topples_x = [log_x100_topples, log_x50_topples, log_x10_topples, log_x5_topples ]
topples_y = [log_y100_topples, log_y50_topples, log_y10_topples, log_y5_topples ]

lengths_x = [log_x100_length, log_x50_length, log_x10_length, log_x5_length ]
lengths_y = [log_y100_length, log_y50_length, log_y10_length, log_y5_length ]






    
plt.rcParams.update({'font.size': 22})
plt.rcParams["font.sans-serif"] = "Helvetica"
plt.rcParams["font.family"] = "serif"

fig, axs = plt.subplots(2,2)
axs[1,1].set_xlim([1,1e2])
axs[0,1].set_xlim([1,2e2])
for ax in axs.flat: 
    ax.set_prop_cycle(cycler('color', ['forestgreen', 'darkmagenta', 'black', 'darkorange']))
    ax.set(ylabel = "Relative frequency")

for data in datas: 
    axs[0,0].loglog(data[0]['Topples'][0],data[0]['Topples'][1], 
       alpha = 0.5,
       label = data[1])
    axs[1,1].loglog(data[0]['Loss'][0][1:-1],data[0]['Loss'][1][1:-1], 
       alpha = 0.5,
       label = data[1])
    axs[1,0].loglog(data[0]['Area'][0],data[0]['Area'][1], 
       alpha = 0.5,
       label = data[1])
    axs[0,1].loglog(data[0]['Length'][0],data[0]['Length'][1], 
       alpha = 0.5,
       label = data[1])
    
#    axs[0,1].set_ylimit(10e-4,10)
#
for idx in range(len(datas)): 
    axs[0,0].plot(datas[idx][0]['Topples'][0],np.exp(fits[idx]["Topples"]["fit"]), 
       linestyle = 'dashed')
    axs[0,1].plot(datas[idx][0]['Length'][0],np.exp(fits[idx]["Length"]["fit"]), 
       linestyle = 'dashed')
    axs[1,0].plot(datas[idx][0]['Area'][0],np.exp(fits[idx]["Area"]["fit"]), 
       linestyle = 'dashed')
    axs[1,1].plot(datas[idx][0]['Loss'][0][1:-1],np.exp(fits[idx]["Loss"]["fit"]),
       linestyle = 'dashed')
#   

axs[0,0].set(xlabel = "Magnitude of avalanche", 
   title = "Relative frequency of avalanche magnitudes")
axs[0,1].set(xlabel = "Length of avalanche",
   title = "Relative frequency of avalanche lengths")
axs[1,0].set(xlabel = "Area of avalanche", 
   title = "Relative frequency of avalanche areas")
axs[1,1].set(xlabel = "Loss of avalanche", 
   title = "Relative frequency of avalanche losses")

for ax in axs.flat: 
    ax.legend(loc = 'best')

fig.subplots_adjust(hspace = 0.35)
plt.show()









