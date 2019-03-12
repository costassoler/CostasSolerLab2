
# coding: utf-8

# In[1]:

import numpy as np

def smooth(s_on,s_off,freqs,inc):
    '''
    ARGUMENTS:
    s_on = Your Online Spectrum
    s_off = your offline spectrum (you make this by 
    running the cells before you use this function)

    inc is the size of the bins (short for incriment)
    
    RETURNS:
    s_on/s_off, which should give you the smoothed line shape
    ''' 
    freqs_sm = np.empty((len(freqs)//inc))
    for i  in range (0, len(freqs)//inc):
        freqs_sm[i] = np.mean(freqs[inc*i:inc*(i+1)])
    sm_off = []
    sm_on = []

    for i in range (0,len(s_on)//inc):
        sm_off.append(np.mean(s_off[i*inc:(i+1)*inc]))
        sm_on.append(np.mean(s_on[i*inc:(i+1)*inc]))

    return (freqs_sm,sm_on,sm_off)

def chi(g_s,g_o,models,start,end,inc):
   
    '''ARGUMENTS:
    g_s and g_o are the observed guide wavelengths when the waveguide is shorted or opened respectively.
    freqs - your frequencies array
    start - the first value you'd like to test for a
    end - the last value you'd like to test for a
    inc - the step size between different test values for a
    RETURNS:
    A[min], where A[min] is the value of a (from equation 9) that produces the minimum chi squared value.'''
    
    A = np.arange(start,end,inc)
 
            
    Obs = (np.array(g_s)+np.array(g_o))/2
    chai = np.empty(models.shape[0])
    for i in range (1,models.shape[0]):
        X = 0
        for j in range(0,models.shape[1]):
            X+=(Obs[j]-models[i,j])**2/models[i,j]
        chai[i] = X
    results = np.where(chai==np.min(chai))
    min = results[0][0]
 
    return A[min]
    
    