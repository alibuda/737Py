# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:00:31 2016

@author: Administrator
"""
#%%
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import os
os.chdir('D:\LearnPy')
import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)
#%%
cols = [4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,31,32,33,34,35,44,45,46,47,49,50,51,52,53,54,55,56,65,66,67,68,69,70,71,72,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,96,98,99,100,101,102,103,104,105,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,146,147,148,149,150,151,152,153,154,155,156,157,174,175,192,193,194,195,196,197,198,199,216,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256]
chunker = pd.read_csv('B-1528_20160328084250.csv',usecols = cols,encoding = 'latin-1')
grouped = chunker.stack().swaplevel(0,1).sortlevel(0)
grouped = grouped.groupby(level = 0)

#%%
def ALPHA(group,p = 30,a = 0.2):
  alpha = (group.rolling(p).max()-group.rolling(p).min())/(group.max()-group.min())
  alpha = alpha.fillna(a)
  return alpha

#%%
def SMOOTH(group,alpha):
  group_smooth = group
  al = alpha[group.name]
  for i,value in enumerate(group):
    if i==0:
      group_smooth[i] = value
    else:
      group_smooth[i] = value*al[i] + group_smooth[i-1]*(1-al[i])
  return group_smooth

#%%
def SFMA(group,p = 30,a = 0.2):
  alpha = (group.rolling(p).max()-group.rolling(p).min())/(group.max()-group.min())
  alpha = alpha.fillna(a)
  group_smooth = group
  for i,value in enumerate(group):
    if i==0:
      group_smooth[i] = value
    else:
      group_smooth[i] = value*alpha[i] + group_smooth[i-1]*(1-alpha[i])
  alpha.name = 'alpha'
  group_smooth.name = 'smooth'
  return group_smooth,alpha

#test = grouped.apply(SFMA)
#alpha = grouped.apply(ALPHA)
#smooth = grouped.apply(SMOOTH,alpha)