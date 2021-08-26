import numpy as np

from numpy import random




class SandPile:
    """SandPile class
    """

    def __init__(self, width, height, threshold=4):
        """Initialize a sandpile with the specified width and height.


        """
        self.width = width
        self.height = height
        self.threshold = threshold

        self.grid = np.zeros((width+2, height+2), dtype=int)
        """By adding 2 to the height and width of the table we can let the edge be
        of the table be the sink for lost sand grains   """
        # We may want to keep track of the overall mass of the sand pile
        # overtime.  The following array will store the masses at each time
        # step (so that `len(self.mass_history)` is equal to the number of time
        # steps the sand pile has been running).
        self.mass_hist = []
        # self.A_mat = np.zeros(self.width,self.height)
        # You probably will want to define other attributes to store statistics.

        # It is good practice to define *all* class attributes in the
        # `__init__` function, even if they get redefined later.  You may want
        # to define variables which are used to keep track of avalanches.

    def drop_sand(self, n=1, sites=None):
        """Add `n` grains of sand to the grid.  Each grains of sand is added to
        a random site.

        Parameters
        ==========

        n: int

          The number of grains of sand of drop at this time step.  If left
          unspecified, defaults to 1.

        site:

          The site on which the grain(s) of sand should be dropped.  If `None`,
          a random site is used.

        """

        if not np.any(sites):
            # print("bug")
            """ If there are no specific sites provided for the grains to be dropped in, then we randomize """
            sites = np.zeros((n,2),dtype= int)

            for i in range(n):

                sites[i] = (random.randint(1,self.width+1),random.randint(1,self.height+1))


        """Drop in the sand!"""
        for site in sites:
            # print(site)
            self.grid[site[0]][site[1]] = self.grid[site[0]][site[1]] + 1
        # print(sites)
        return sites[0]



    def mass(self):
        """Return the mass of the grid."""
        # print(self.grid[1:self.height+1,1:self.height+1])
        return np.sum(self.grid[1:self.height+1,1:self.height+1])
        # raise NotImplementedError()
    def av_topp(self, A_mat):
        """ Function that returns the total number of topples in an avalanche given the
        avalanche matrix (see comments on avalanche method)  """
        return np.sum(A_mat)


    def av_loss(self, A_mat):
        """ Function that returns the total number of grains lost in an avalanche given the
        avalanche matrix """
        loss = 0

        # print(A_mat)
        for x in range(self.width):
            loss += A_mat[x,0]

            loss += A_mat[0,x]

            loss += A_mat[x,self.width-1]

            loss += A_mat[self.width-1,x]
            #corners will be counted twice, we do not need to account for the seperately

        return loss

    def av_area(self, A_mat):
        """Function that returns the area of an avalanche given the avalanche matrix"""
        area = 0
        for x in range(self.width):
            for y in range(self.height):
                if A_mat[x,y]:
                    area += 1
        return area

    def av_length(self, A_mat, origin):
        """ Function returns the length of an avalanche - the distance between the first avalanche and that furtherst
        from it- givne the avalanche matrix"""
        x = origin[0]
        y = origin[1]


        distances = []
        for i in range(self.width):
            for j in range(self.height):
                if A_mat[i,j]:
                    distances.append(abs(x-i)+abs(y-j))
        return max(distances)

    def topple(self, site):
        """Topple the specified site."""
        self.grid[site] = self.grid[site]-4
        self.grid[site[0]+1,site[1]] += 1
        self.grid[site[0]-1,site[1]] += 1
        self.grid[site[0],site[1]+1] += 1
        self.grid[site[0],site[1]-1] += 1
        # raise NotImplementedError()

    def avalanche(self, origin):
        # A_mat = np.zeros(self.width,self.width)

        # sys.setrecursionlimit(10000)

        """Run the avalanche causing all unstable sites to topple and store the avalanche data
        in A_mat

        """

        """This will be a recursive function, i.e. if the toppling within the first iteration cause
        more unstalbe states, we will have to call avalanche again"""

        """The array A_mat (avalanche matrix) will be used to keep track of which sites have been toppled, so that later we
        can calculate the overall number of topples and also the area of the avalanche """

        """ origin is the location of the initial unstable state, we will need this to find the length of the avalanche"""

        """The return tuple is of the form (grid, A_mat, origin)."""

        A_mat = np.zeros((self.width,self.height), dtype = int)
        while self.grid[1:self.width+1,1:self.height+1].max() >= 4:
            for site in np.argwhere(self.grid[1:self.width+1,1:self.height+1] >= 4):
                A_mat[site[0],site[1]] += 1
                # print(site)
                site = (site[0]+1,site[1]+1)
                # print(site)


                self.topple(site)
                # print(self.grid)


        # topples = self.av_topp(A_mat)

        return (self.grid, A_mat, origin)




        # raise NotImplementedError()

    def driv_force(self, n = 1, time_step = 1, runtime = 10):
        """This is a function that loops over time and adds n grains of sand
        to the grid at random sites at each time step. This is only really used for
        testing purposes, the main looping functions are the ones found in the system.py file  """

        time = 0
        while time < runtime:
            self.drop_sand(n)
            self.mass_hist.append(self.mass())
            time += time_step


    # You are free to define more methods within this class
