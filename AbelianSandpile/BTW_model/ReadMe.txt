The sandpile.py contains the SandPile class and all its methods. system.py contains all functions used to run the simulation, i.e. the simulation itself, the concept of time etc. are not part of the sandpile class. 

main.py was only used to call function from the system.py file, then turn the recorded data into relative frequency distributions. test.py was used to test function and methods. There is a few lines of code in there that will familarize you with the method/variable names and required arguments. 

Note that the grid attribute of the SandPile class is not of shape (self.width,self.height) but (self.width+2,self.height+2). Then the actual table is just this minus the edges. So if you want to interact with the table as oppossed to the grid, you must use self.grid[1:self.width+1,1:self.height+1].

plot.py was used to plot the data. Obviously sandpile.py and system.py are the most heavily commented. 

The data files included are what I used to create the distributions found in the logbook. Obviously it takes a while to run 10^5 avalanches on a 100x100 grid, so I exported the data as a pickle file. You can use the pickle library with pickle.load(infile) to have a look at this data yourself.  
