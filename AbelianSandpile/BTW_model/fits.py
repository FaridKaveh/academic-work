#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:21:48 2019

@author: farid
"""

import numpy as np
import pickle 
#import numpy.polynomial.polynomial as poly
#import math

infile_1 = open('5x5data', 'rb')
infile_2 = open('10x10data', 'rb')
infile_3 = open('50x50data', 'rb')
infile_4 = open('100x100data', 'rb')

data_5  = pickle.load(infile_1)
data_10 = pickle.load(infile_2)
data_50 = pickle.load(infile_3)
data_100 = pickle.load(infile_4)

infile_1.close()
infile_2.close()
infile_3.close()
infile_4.close()

to_fit = [data_5, data_10, data_50, data_100]

#def eval(x, coeff): 
#    return coeff[1] + coeff[0]*x

def log_poly_fit(x, y, degree):
    
    """ Here we use polynomial regression to find a fit to y, then find the R^2 value """
    log_x = np.log(x)
    log_y = np.log(y)
    fit_dict = {} 
    
    avg = np.mean(log_y)
    
    coeffs = np.polyfit(log_x, log_y, deg = degree, w = np.sqrt(y), full = False, cov = True)
    var_arr= []
    for idx in range(coeffs[1].shape[1]):
        var_arr.append(coeffs[1][idx][idx])
    var_arr.reverse() 
    fit_dict['coefficients'] = coeffs[0].tolist()
    fit_dict['coefficients'].reverse()
    fit_dict['variances'] = var_arr 
    
    
    fit = np.zeros(log_y.shape, dtype = float)
    for idx in range(len(fit_dict['coefficients'])):
        fit += fit_dict['coefficients'][idx]*(log_x**idx)
        
#    fit = fit_dict['coefficients'][1]+ fit_dict['coefficients'][0]*log_x
#    print(fit)
    


    fit_dict['fit'] = fit 
  
  
    
    return fit_dict

fit_5 = {}
fit_10 = {} 
fit_50 = {} 
fit_100 = {} 

to_plot = [fit_5, fit_10, fit_50, fit_100]

"""Finding linear fits for the data and exporting"""

for idx in range(len(to_fit)): 
    for key in to_fit[idx]:
        
        
        if key != "Loss":
            to_plot[idx][key] = log_poly_fit(to_fit[idx][key][0],
                   to_fit[idx][key][1],1)

        else: 
            to_plot[idx][key] = log_poly_fit(to_fit[idx][key][0][1:-1], 
                                to_fit[idx][key][1][1:-1],2)
            
            
#print(to_plot[3]['Loss']['coefficients'])
outfile = open("fitsVar", 'wb')
pickle.dump(to_plot, outfile)
outfile.close()
    
    
    
    
    
    