# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 07:01:38 2019

@author: Abirmoy
"""

import pandas as pd

#1

## CREATE A DATAFRAME WITH AN x COLUMN CONTAINING VALUES FROM -10 TO 10
#
#df = pd.DataFrame({'x':range(-10,11)})
#
## ADD A y COLUMN BY APPLYING THE SOLVED EQUATION TO X
#
#df['y'] = (3*df['x'] - 4) / 2 # same ase y = (3x-4)/2
#
## DYSPLAY THE DATE FRAME
#
#print(df)


################################################################################
#We can also plot these values to visualize the relationship between x and 
#y as a line. For this reason, equations that describe a relative 
#relationship between two variables are known as linear equations:
#

#%matplotlib inline
from matplotlib import pyplot as plt

plt.plot(df.x, df.y, color='grey', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
























