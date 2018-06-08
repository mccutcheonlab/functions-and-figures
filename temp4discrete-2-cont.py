# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:55:03 2018

@author: James Rig
"""
import os
import numpy as np
import JM_general_functions as jmf
import matplotlib.pyplot as plt

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



cwd = os.getcwd()
metafile = 'QPP1_metafile.txt'
A,header = jmf.metafilereader(cwd + '\\' + metafile)


medfolder = 'R:\\DA_and_Reward\\fn55\\QPP-1 (fn55)\\20-05-18 Conditioning 4\\'
medfile=A[110][0]
filename=medfolder+medfile

onsets, offsets = jmf.medfilereader(filename, 
                                    varsToExtract=["b","c"],
                                    remove_var_header = True)


t, y = discrete2continuous(onsets, offset=offsets, fs=200)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(t, y)


#y = y[:100000]

Y = np.fft.rfft(y)
freq = np.fft.rfftfreq(len(y), t[1] - t[0])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-0.1,30)
ax.set_ylim(-1000, 4000)
ax.plot(freq, np.abs(Y))



