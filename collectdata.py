import ugradio
import numpy as np
import matplotlib.pyplot as plt


def collect(volt_range, blocks, numrepeat, name):
    """
    ARGUMENTS:
    volt_range: this is the voltage range, which we keep at 100 mV **make sure this is a string!**
    blocks: this is the number of data sets/blocks you'd like to write into a single file
    numrepeat: This is the number of times you'd like to write data files (i.e. the amount of data fileyou     want) 
    name: this is what you want your files to be named (they come out looking like: name0.npz,name1.npz,       etc)
    RETURNS:
    this doesn't return anything to the command line, but you will end up with data files in the directory     from which you ran this. 
    """
    

    for i in range (0,numrepeat):
        data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True, nblocks=blocks)
        np.savetxt(name+str(i),data)

def insert_upper(volt_range):
    data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True)
    np.savetxt('uppertestsig', data)

    return np.loadtxt('uppertestsig')


def insert_lower(volt_range):
    data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True)
    np.savetxt('lowertestsig', data)

    return np.loadtxt('lowertestsig')



