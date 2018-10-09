# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:24:36 2018

@author: jaimeHP
"""
import numpy as np

pre_events = [2, 3.4, 45, 79, 101]
events = [3, 81, 101.1]

latency = []

for event in events:
    latency.append(np.abs([lat-event for lat in pre_events if lat-event<0]).min())
#        idx = (np.abs(event - on)).argmin()
#        
#        latency.append([event-lat for lat in pre_events][0])
#    latency = [event for event in events]
#    
#event=3
#np.abs([lat-event for lat in pre_events]).min()