# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:37:32 2023

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-poster')
%matplotlib inline 
# sampling rate
sr = 2000
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 4*np.sin(6*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (10, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()