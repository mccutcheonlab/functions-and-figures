# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:36:04 2018

@author: jaimeHP
"""

import moviepy.editor as mv
import numpy as np


filename = 'C:\\Users\\jaimeHP\\Dropbox\\Shared and resource folders\\Photometry_corrupted\\Giulia-180716-115500\\PPP3-180705-135030_Giulia-180716-115500_Cam1.avi'

clip = mv.VideoFileClip(filename).subclip(600,1200)

frames_to_extract = [x*100 for x in range(0,60)]
frame_array = [x for i, x in enumerate(clip.iter_frames()) if i in frames_to_extract]

subclip = mv.ImageSequenceClip(frame_array, fps=1)

subclip.write_videofile('temp_movie.avi', codec='avi')
