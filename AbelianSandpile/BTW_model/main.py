#!/usr/bin/env python3
"""Sandpile Lab
============

This is the main file from which we run all the various routines in the
sandpile lab.

"""
import pathlib
import time

import numpy as np


from sandpile import SandPile
from system import system_timed, system_stable, first_avalanche_dist, stable_avalanches


import pickle



# def main():
#     # Make sure that the output/ directory exists, or create it otherwise.
#     output_dir = pathlib.Path.cwd() / "output"
#     if not output_dir.is_dir():
#         output_dir.mkdir()
#
#     # This is the main part of the code.  Since this lab has quite a few
#     # distinct parts, it will be a good idea to define functions above that do
#     # particular parts of the lab.
#
#     # Example Plotting
#     ########################################
#     # Here is a simple example of a plotting routine.  We create a standard
#     # line plot, and also a histogram.
#
#     # First, we create an array of x values, and compute the corresponding y
#     # values.
#     x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
#     y = np.sin(x) / x
#     # We create the new figure with 1 subplot (the default), and store the
#     # Figure and Axis object in `fig` and `ax` (allowing for their properties
#     # to be changed).
#     fig, ax = pyplot.subplots()
#     ax.plot(x, y)
#     ax.set_title("Plot of sin(x) / x")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     # Matplotlib by default does a good job of figuring out the limits of the
#     # axes; however, it can fail sometimes.  This allows you to set them
#     # manually.
#     ax.set_ylim([-0.5, 1.1])
#     fig.savefig("output/example.pdf")
#     pyplot.close(fig)
#
#     # Now for the histogram.  We generate some random data
#     data = np.random.randn(1000000)
#     fig, ax = pyplot.subplots()
#     ax.hist(data)
#     ax.set_title("Histogram of random data")
#     ax.set_xlabel("Value")
#     ax.set_ylabel("Frequency")
#     fig.savefig("output/example_histogram.pdf")
#     pyplot.close(fig)
#
#     # In this lab, you'll also want to show what the grid looks like.  This can
#     # be done with `imshow`.
#     data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#     fig, ax = pyplot.subplots()
#     ax.imshow(data)
#     ax.set_title("Grid plot")
#     fig.savefig("output/example_grid.pdf")
#     pyplot.close(fig)

# data = system_stable(6,6)
#
# print(len(data[-1]))

# fig, (ax1, ax2) = pyplot.subplots(1,2)
# plot1 = ax1.imshow(Pile_i)
# plot2 = ax2.imshow(Pile_f)
# ax1.set_ylabel("y")
# ax1.set_xlabel("x")
# ax2.set_ylabel("y")
# ax2.set_xlabel("x")
# pyplot.show()
#
# sandpile = SandPile(6,6,4)
# for x in range(1,sandpile.width+1):
#     for y in range(1,sandpile.height+1):
#         sandpile.grid[x][y] = 4
#
#         print(sandpile.grid[1:sandpile.width+1,1:sandpile.height+1])
# sandpile.avalanche((3,3))
# print(sandpile.grid)

""" This is the section where I compiled the data for 5x5, 10x10. 50x50 and 100x100 grids and saved them onto a pickle file.
It would be possible to do a lot of this code in a for loop if I created a list of the dictionaries, but I thought that this way
it would be clearer what I'm doing. Obviously running this code takes a long time. (due to the first 4 lines, which calculate the
properties of 1e5 avalanches for each grid size, initiating each pile in its statistically stable state)"""

data_1 = stable_avalanches(5, 5, 45, int(1e5))
data_2 = stable_avalanches(10,10, 198, int(1e5))
data_3 = stable_avalanches(50,50, 5235, int(1e5))
data_4 = stable_avalanches(100,100, 21100, int(1e5))


dist_dict_1 = {'Topples': [] , 'Area': [],
'Loss': [], 'Length': [] }
dist_dict_2 = {'Topples': [] , 'Area': [],
'Loss': [], 'Length': [] }
dist_dict_3 = {'Topples': [] , 'Area': [],
'Loss': [], 'Length': [] }
dist_dict_4 = {'Topples': [] , 'Area': [],
'Loss': [], 'Length': [] }



for avalanche in data_1[0:len(data_1)]:
    dist_dict_1['Topples'].append(avalanche[0])

    dist_dict_1['Area'].append(avalanche[1])
    dist_dict_1['Loss'].append(avalanche[2])
    dist_dict_1['Length'].append(avalanche[3])
for avalanche in data_2[0:len(data_2)]:
    dist_dict_2['Topples'].append(avalanche[0])

    dist_dict_2['Area'].append(avalanche[1])
    dist_dict_2['Loss'].append(avalanche[2])
    dist_dict_2['Length'].append(avalanche[3])
for avalanche in data_3[0:len(data_3)]:
    dist_dict_3['Topples'].append(avalanche[0])

    dist_dict_3['Area'].append(avalanche[1])
    dist_dict_3['Loss'].append(avalanche[2])
    dist_dict_3['Length'].append(avalanche[3])
for avalanche in data_4[0:len(data_4)]:
    dist_dict_4['Topples'].append(avalanche[0])

    dist_dict_4['Area'].append(avalanche[1])
    dist_dict_4['Loss'].append(avalanche[2])
    dist_dict_4['Length'].append(avalanche[3])

# print(dist_dict['Loss'], data[-1])
dist_dict_1['Topples'] =  np.unique(dist_dict_1['Topples'], return_counts = True)
dist_dict_1['Area'] =  np.unique(dist_dict_1['Area'], return_counts = True)
dist_dict_1['Loss'] =  np.unique(dist_dict_1['Loss'], return_counts = True)
dist_dict_1['Length'] =  np.unique(dist_dict_1['Length'], return_counts = True)

dist_dict_2['Topples'] =  np.unique(dist_dict_2['Topples'], return_counts = True)
dist_dict_2['Area'] =  np.unique(dist_dict_2['Area'], return_counts = True)
dist_dict_2['Loss'] =  np.unique(dist_dict_2['Loss'], return_counts = True)
dist_dict_2['Length'] =  np.unique(dist_dict_2['Length'], return_counts = True)

dist_dict_3['Topples'] =  np.unique(dist_dict_3['Topples'], return_counts = True)
dist_dict_3['Area'] =  np.unique(dist_dict_3['Area'], return_counts = True)
dist_dict_3['Loss'] =  np.unique(dist_dict_3['Loss'], return_counts = True)
dist_dict_3['Length'] =  np.unique(dist_dict_3['Length'], return_counts = True)

dist_dict_4['Topples'] =  np.unique(dist_dict_4['Topples'], return_counts = True)
dist_dict_4['Area'] =  np.unique(dist_dict_4['Area'], return_counts = True)
dist_dict_4['Loss'] =  np.unique(dist_dict_4['Loss'], return_counts = True)
dist_dict_4['Length'] =  np.unique(dist_dict_4['Length'], return_counts = True)


# print(dist_dict['Topples'])

""" Dictionaries to save the relative freq data"""
Rel_freq_data_5 = {'Topples': [] , 'Area': [], 'Loss': [], 'Length': [] }
Rel_freq_data_10 = {'Topples': [] , 'Area': [], 'Loss': [], 'Length': [] }
Rel_freq_data_50 = {'Topples': [] , 'Area': [], 'Loss': [], 'Length': [] }
Rel_freq_data_100 = {'Topples': [] , 'Area': [], 'Loss': [], 'Length': [] }


"""These next four loops are turning actualy frequencies to relative frequencies to be plotted """

for key in Rel_freq_data_5:
    Rel_freq_data_5[key] = [dist_dict_1[key][0],dist_dict_1[key][1]/int(1e5)]
for key in Rel_freq_data_10:
    Rel_freq_data_10[key] = [dist_dict_2[key][0],dist_dict_2[key][1]/int(1e5)]
for key in Rel_freq_data_50:
    Rel_freq_data_50[key] = [dist_dict_3[key][0],dist_dict_3[key][1]/int(1e5)]
for key in Rel_freq_data_100:
    Rel_freq_data_100[key] = [dist_dict_4[key][0],dist_dict_4[key][1]/int(1e5)]


outfile_1 = open('5x5data', 'wb')
outfile_2 = open('10x10data', 'wb')
outfile_3 = open('50x50data', 'wb')
outfile_4 = open('100x100data', 'wb')

pickle.dump(Rel_freq_data_5, outfile_1)
pickle.dump(Rel_freq_data_10, outfile_2)
pickle.dump(Rel_freq_data_50, outfile_3)
pickle.dump(Rel_freq_data_100, outfile_4)

outfile_1.close()
outfile_2.close()
outfile_3.close()
outfile_4.close()

# dist = avalanche_dist(10, 10, 10)
#
# print(dist['Topples'])
# fig, ((ax1,ax2) , (ax3, ax4)) = pyplot.subplots(2,2)
# ax1.plot(Rel_freq_data['Topples'][0][1:],Rel_freq_data['Topples'][1][1:])
# ax1.set_xlabel("Number of topples")
# ax1.set_ylabel("Relative freq")
#
# ax2.plot(Rel_freq_data['Area'][0],Rel_freq_data['Area'][1])
# ax2.set_xlabel("Number of unique sites toppled (area)")
# ax2.set_ylabel("Relative freq")
#
# ax3.plot(Rel_freq_data['Loss'][0],Rel_freq_data['Loss'][1])
# ax3.set_xlabel("Mass of sand lost to the edges")
# ax3.set_ylabel("Relative freq")
#
# ax4.plot(Rel_freq_data['Length'][0],Rel_freq_data['Length'][1])
# ax4.set_xlabel("Length of avalanche")
# ax4.set_ylabel("Relative freq")
# pyplot.show()
# fig, ax = pyplot.subplots()
# ax.plot(Rel_freq_data['Loss'][0],Rel_freq_data['Loss'][1])
# ax.set_xlabel("Mass of sand lost to the edges")
# ax.set_ylabel("Relative freq")
# pyplot.show()




#
# if __name__ == "__main__":
#     main()
