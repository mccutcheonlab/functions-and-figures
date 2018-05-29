# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:42:33 2018

@author: James Rig
"""

import JM_general_functions as jmf
import matplotlib.pyplot as plt
import numpy as np

medfile = 'C:\\Users\\James Rig\\Documents\\GitHub\\functions-and-figures\\!2018-05-21_13h55m.Subject QPP1.5197'

licksA_on, licksA_off = jmf.medfilereader(medfile, ['b', 'c'], remove_var_header = True)
licksB_on, licksB_off = jmf.medfilereader(medfile, ['e', 'f'], remove_var_header = True)

lickdataA = jmf.lickCalc(licksA_on, offset=licksA_off, adjustforlonglicks='interpolate')

lickdataB = jmf.lickCalc(licksB_on, offset=licksB_off, adjustforlonglicks='interpolate')

f1 = plt.figure()
ax = f1.add_subplot(1,2,1)

ax.hist(lickdataA['licks'])

lickdataA = jmf.lickCalc(licksA_on, offset=licksA_off)

f1 = plt.figure()
ax = f1.add_subplot(1,2,1)

ax.hist(lickdataA['licks'])
