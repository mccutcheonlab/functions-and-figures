# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import JM_custom_figs as jmf

#a = [[2,4,6,8,3,2.2,8.7, 3, 1.1],
#     [3,5,8,7]]

# MALES SALINE
# Acquisition
exploration_left_sal_M = [27.18,26.69,19.61,18.17,16.09,30.06,36.54,38.87,24.76,26.86,34.15,0,30.57,38.28]
exploration_right_sal_M = [52.44,21.21,33,35.8,37.41,25.45,31.2,15.71,20.07,28.24,27.82,6.97,40.93,14.52]
# Retention
exploration_fam_sal_M = [28.8,13.56,27.5,11.81,9.06,14.66,21.8,20.62,5.76,17.1,15.16,0,6.18,17.46]
exploration_nov_sal_M = [29.5,17.99,28.96,26.71,16.97,31.82,22.29,20.03,29.02,19.79,18.7,25.74,57.62,29.96]
DI_sal_M = [0.01,0.14,0.03,0.39,0.3,0.37,0.01,-0.01,0.67,0.07,0.1,1,0.81,0.26]

# MALES PCP
# Acquisition
exploration_left_pcp_M = [19.85,29.53,25.52,36.45,19.56,10.28,31.46,12.52,16.28,19.52,27.91,25.59,23.98,29.35,19.89,23.88]
exploration_right_pcp_M = [30.4,22.96,13.76,18.12,20.22,21.21,24.68,21.6,49.08,25.87,9.76,39.46,11.43,20.13,16.41,27.11]
# Retention
exploration_fam_pcp_M = [6.49,7.89,13.81,26.66,29.22,9.28,17.39,18.82,22.95,20.86,11.55,35.84,0.9,13.38,5.68,7.84]
exploration_nov_pcp_M = [13.32,23.52,35.97,8.81,18.53,9.59,38.83,18.02,22.75,44.65,29.64,24.91,2,27.41,15.21,27.35]
DI_pcp_M = [0.34,0.5,0.45,-0.5,-0.22,0.02,0.38,-0.02,0,0.36,0.44,-0.18,0.38,0.34,0.46,0.55]


barcolors = ['#AFDBD5','#AFDBD5','#AFDBD5','#AFDBD5']
dataMnorAcq = [[exploration_left_sal_M, exploration_right_sal_M], [exploration_left_pcp_M, exploration_right_pcp_M]]
labels = ['salL','salR', 'pcpL', 'pcpR']
#ax, barx, barlist, sclist = barscatter(dataMnorAcq, transpose=False, paired=False, barfacecolor=barcolors, barfacecoloroption='individual',  ylabel='Time (s)', barlabels=labels) 

dataMnorAcq2 = [[exploration_left_sal_M, exploration_right_sal_M], [exploration_fam_sal_M, exploration_nov_sal_M]]

data3 = [exploration_left_sal_M, exploration_right_pcp_M]
#newdata={}
#for i in [exploration_left_sal_M, exploration_right_sal_M, exploration_fam_sal_M, exploration_nov_sal_M]:
#    
#def data2objsimple(data):
#    
#    obj = np.array(data, dtype=np.object)
##    for i,x in enumerate(data):
##        obj[i] = np.array(x)  
#    return obj
#
#zzz = data2objsimple(exploration_left_sal_M)
#yyy = data2objsimple(exploration_right_sal_M)
#aaa = data2objsimple(exploration_left_pcp_M)
#bbb = data2objsimple(exploration_right_pcp_M)
#
#www = np.ndarray((2,2), dtype=np.object)
#for idx1, dim1 in enumerate([zzz, yyy]):
#    for idx2, dim2 in enumerate([aaa, bbb]):
#        www[idx1][idx2] = print(idx)
##    www[idx] = array
#
#data = dataMnorAcq2
#data2 = dataMnorAcq
#dim = np.ndim(data)



#if dim == 1:
#    try:
#        len(data[0])
#        dim = 2
#        print('Extra dimension', dim)
#    except TypeError:
#        print('Fully flattened - one dimension')
#
#if dim == 2:
#    try:
#        len(data[0][0])
#        print('Extra dimension')
#    except TypeError:
#        print('Two dimensions total')
            
#converteddata = 
#        
#dataMnorAcq
#
#
#jmf.barscatter(dataMnorAcq2, barfacecolor=barcolors, barfacecoloroption='individual',  ylabel='Time (s)', barlabels=labels)



jmf.barscatter(data3, spaced = True, spaceX=0.1,unequal=True, barfacecolor=barcolors, barfacecoloroption='individual',  ylabel='Time (s)', barlabels=labels)