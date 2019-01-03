# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:57:18 2018

@author: jaimeHP
"""

import matplotlib.pyplot as plt

import numpy as np

red = 0.1607843137254902
green = 0.8046875
blue = 0.35546875

loudo_color = [red, green, blue]
yellow = [1, 1, 0]

redx = 1
greenx = 0.5
bluex = 0.8


booker_color = [redx, greenx, bluex]


f, ax = plt.subplots()

    
ax.scatter(1,1, s=1000, color=loudo_color)
ax.scatter(2,1, s=1000, color=booker_color)
ax.scatter(3,2, s=1000, color='#29CE5B')
ax.set_xlim([0,4])
ax.set_ylim([0,3])