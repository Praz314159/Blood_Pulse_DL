'''
This is a naive implementation of a pytorch neural network, using the dual diameter blood pulse pressure waveform data. 

'''

# Packages 
import numpy as np
import torch as flame
import torch.nn as nn 
import torch.nn.functional as func
import random as rd 
import xlrd 
import panndas as pd 

#read in data 

data = pd.read_excel(open('Features_fulldata.xlsx', 'rb'))
#reading execl file (find out what 'rb' means ... 

data.astype('float64').dtypes #homogenizing data type 
pure_data = data.to_numpy() #converting to numpy array
pure_data = pure_data[0:,1:] #removing first col containing index number 




