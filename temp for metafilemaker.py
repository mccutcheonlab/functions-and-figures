# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:14:19 2018

@author: jaimeHP
"""

import JM_general_functions as jmf

xlfile = 'R:\\DA_and_Reward\\gc214\\PPP3\\PPP3.xlsx'
metafile = 'testcsv'

jmf.metafilemaker(xlfile, metafile, sheetname='PPP3_metafile', fileformat='txt')

