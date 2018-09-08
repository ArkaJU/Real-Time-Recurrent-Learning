import pandas as pd                        #importing necessary libraries to read the excel file
import numpy as np
df = pd.read_excel('Helicopter_Original.xlsx')         


n = 50000
z = df.sample(n)                                 #randomly sampling from the dataframe 
x = z.iloc[:,0:7]                                #first 7 columns are inputs
x = np.array(x).astype(np.float32)
mean = np.mean(x, axis=0)                        #columnwise mean and 
sd = np.std(x, axis=0)                           #standard deviation
mean = mean.reshape(7, 1)
sd = sd.reshape(7, 1)
m = mean[0:5]                                                                                 
s = sd[0:5]


def standardise(Z, t='x'):                      #to standardise the data(basically pre-processing)
    if t == 'y':
        Z = (Z - m)/s
    else:
        Z = (Z - mean)/sd
    return Z   


def reverse_standardise(Z, t='x'):              #to reverse-standardise the data
    if t == 'y':
        Z = (Z * s) + m 
    else:
        Z = (Z * sd) + mean
    return Z 
