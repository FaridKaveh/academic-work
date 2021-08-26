import pathlib
import numpy as np
from sandpile import SandPile




""" This file just defines some functions that actually run the simulation as described in the BTW model"""





def system_timed(width, height, end_time):

    """ system_timed runs the simulation with t_step = 1 up to end_time, with grains of sand dropping and possible avalanches in between,
    it will return a list of tuples where each element of the list represents an avalanche and the elements of
    the tuple are the (Topples, Area, Loss, Length) of that avalanche. There will be one final element to the returned list,
    which will be the mass_history of the grid."""
#
#    avalanches = []
    sandpile = SandPile(width, height)
    time = 0

    while time < end_time:
        site = sandpile.drop_sand()
#        avalanched = sandpile.avalanche()
        sandpile.avalanche(site)
        sandpile.mass_hist.append(sandpile.mass())
#       print(len(sandpile.mass_hist))

#        if avalanched[2]:
#                grid = avalanched[0]
#                A_mat = avalanched[1]
#                origin = avalanched[2]
#
#
#
#
#
#                avalanches.append((sandpile.av_topp(A_mat),sandpile.av_area(A_mat),
#                    sandpile.av_loss(A_mat), sandpile.av_length(A_mat,origin)))

        time = time + 1
#    avalanches.append(sandpile.mass_hist)

    return sandpile.mass_hist

def system_stable(width, height):

    """system_stable runs the simulation until a statistically stable state has been reached. In other words, end_time
    is not accepted as an argument. The returned value will be the same. """

    avalanches = []
    sandpile = SandPile(width, height)
    time = 0
    max_m = 0
    count = 0 #count is the variable that keeps track of how many steps max{mass_hist} has remained constant
    while True:
        site = sandpile.drop_sand()
        avalanched = sandpile.avalanche(site) #avalanched = (grid, A_mat, origin)

        sandpile.mass_hist.append(sandpile.mass())


        if max_m < sandpile.mass():
            max_m = sandpile.mass()
            count = 0
        else:
            count += 1


        # if np.any(avalanched[1]):
        #         grid = avalanched[0]
        #         A_mat = avalanched[1]
        #         origin = avalanched[2]





                # avalanches.append((sandpile.av_topp(A_mat),sandpile.av_area(A_mat),
                    # sandpile.av_loss(A_mat), sandpile.av_length(A_mat,origin)))
        if count == 4*width:

            return sandpile.mass_hist



def first_avalanche_dist(width, height, n):

    """ The first_avalanche_dist function runs the simulation n times up until the first avalanche occurs,
    it then records these and returns as a dictionary """


    dist = { 'Topples': [] , 'Area': [], 'Loss': [], 'Length': []}
    i = 0
    while i < n:

        sandpile = SandPile(width, height)


        while True:
            sandpile.drop_sand()
            avalanched = sandpile.avalanche() #avalanched = (grid, A_mat, origin)

            sandpile.mass_hist.append(sandpile.mass())

            if avalanched[2]:
                dist['Topples'].append(sandpile.av_topp(avalanched[1]))
                dist['Area'].append(sandpile.av_area(avalanched[1]))
                dist['Loss'].append(sandpile.av_loss(avalanched[1]))
                dist['Length'].append(sandpile.av_length(avalanched[1],avalanched[2]))
                print(sandpile.grid)
                break

        i += 1


    return dist




def stable_avalanches(width, height, stable_mass, n):
    """ stable_avalanches gives us data sets for avalaches that occur in a statistically stable state by initiating the
    lattice with a mass which is close to or at such a state and then running the simulation up unti we have n data points
    the returned list is similar to that in system_timed and system_stable (see comments there)"""

    sandpile = SandPile(width,height)
    sandpile.drop_sand(n = stable_mass)


    avalanches = [] #the returned list
    i = 0

    sandpile.avalanche((0,0)) #origin of this avalanche does not matter, we jut call it so the system starts in a stable config

    while True:
        site = sandpile.drop_sand()
        # print(sandpile.grid)
        avalanched = sandpile.avalanche(site) #avalanched = (grid, A_mat, origin)

        sandpile.mass_hist.append(sandpile.mass())

        if np.any(avalanched[1]):

                grid = avalanched[0]
                A_mat = avalanched[1]
                origin = avalanched[2]


                # if sandpile.av_topp(A_mat) <  5:
                #     print("BUG")

                avalanches.append((sandpile.av_topp(A_mat),sandpile.av_area(A_mat),
                    sandpile.av_loss(A_mat), sandpile.av_length(A_mat,origin)))
        if len(avalanches) == n:
            avalanches.append(sandpile.mass_hist)

            return avalanches
