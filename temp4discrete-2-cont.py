# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:55:03 2018

@author: James Rig
"""
import os
import numpy as np
import JM_general_functions as jmf
import matplotlib.pyplot as plt

from statsmodels.nonparametric.smoothers_lowess import lowess

def discrete2continuous(onset, offset=[], nSamples=[], fs=[]):
    
    try:
        fs = int(fs)
    except TypeError:
        isis = np.diff(onset)
        fs = int(1 / (min(isis)/2)) 
    
    if len(nSamples) == 0:
        nSamples = int(fs*max(onset))    
    
    outputx = np.linspace(0, nSamples/fs, nSamples)
    outputy = np.zeros(len(outputx))
    
    if len(offset) == 0:
        for on in onset:
            idx = (np.abs(outputx - on)).argmin()
            outputy[idx] = 1
    else:
        for i, on in enumerate(onset):
            start = (np.abs(outputx - on)).argmin()
            stop = (np.abs(outputx - offset[i])).argmin()
            outputy[start:stop] = 1

    return outputx, outputy



#cwd = os.getcwd()
#metafile = 'QPP1_metafile.txt'
#A,header = jmf.metafilereader(cwd + '\\' + metafile)


medfolder = 'R:\\DA_and_Reward\\kp259\\DPCP2\\'
medfile='!2017-10-06_08h27m.Subject dpcp2.7'
filename=medfolder+medfile

onsets, offsets = jmf.medfilereader(filename, 
                                    varsToExtract=["e","f"],
                                    remove_var_header = True)


#t, y = discrete2continuous(onsets, offset=offsets, fs=200)

lickspersecond = np.histogram(onsets, bins=3600, range=(0,3600))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(t, y)
#
#
#y = y[:100000]


#y = lickspersecond[0]
#t = lickspersecond[1]

#Y = np.fft.rfft(y)
freq = np.fft.rfftfreq(len(y), t[1] - t[0])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


ax.semilogx(freq, smoothedY)


smoothedY = lowess(np.abs(Y), freq, is_sorted=True, frac=0.025, it=0)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#ax.set_xlim(-0.1,10)
#ax.set_ylim(0, 2000)


ax.plot(freq, smoothedY)



