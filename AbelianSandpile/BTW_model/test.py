import pathlib
import time

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot

from sandpile import SandPile
from system import system_timed, system_stable, first_avalanche_dist, stable_avalanches


"""This file is for testing different parts of the code and seeing how/whether things work. The first batch of code that
is already here is the one that simulates an avalanche of a 7x7 grid starting with all site but the central one
at a mass of 3, and an unstalbe central site with mass 4 (as described in the logbook). It the prints the avalanche matrix as well (T, A, R, L)"""

sandpile = SandPile(7,7)
sandpile.grid[1:sandpile.width+1,1:sandpile.height+1] = 3 * np.ones((sandpile.width,sandpile.height))
site = sandpile.drop_sand(sites = [(4,4)])
A_mat = sandpile.avalanche(site)[1]
print(A_mat,sandpile.av_topp(A_mat),sandpile.av_area(A_mat),sandpile.av_length(A_mat, site), sandpile.av_loss(A_mat))

# sandpile = SandPile(10,10)

"""This next bit will plot the histogram for the mass of a 10x10 grid until it reaches its stable state"""

stable_10 = system_stable(10,10)
pyplot.plot(stable_10)
pyplot.show()
