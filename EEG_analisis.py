# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:40:08 2021

@author: ianja
"""

import numpy as np
import pandas as pd 

df = pd.read_excel('EEG_ian.xlsx')
lista_carac=[]
index=[]
v=np.array([])
signal_strengt=np.array([0])
attention=np.array([])
meditation=np.array([])
delta=np.array([])
theta=np.array([])
low_alpha=np.array([])
high_alpha=np.array([])
low_beta=np.array([])
high_beta=np.array([])
low_gamma=np.array([])
high_gamma=np.array([])

a1=0
z=0
list_of_single_column = df['EEG'].tolist()

print("the list of a single column from the dataframe\n",
        list_of_single_column,
        "\n",
        type(list_of_single_column))

for i in range(len(list_of_single_column)):
    a=list_of_single_column[i].split(',')
    lista_carac.append(a)
# signal strength0, attention1, meditation2, delta3, theta4, low alpha5, 
# high alpha6, low beta7, high beta8, low gamma9, high gamma 10

for i in range(len(lista_carac)):
        az=int(lista_carac[i][0])        
        np.append(signal_strengt,az)
        #     np.append(attention,az)
        #     np.append(meditation,az)
        #     np.append(delta,az)

        # elif z == 4:
        #     np.append(theta,az)

        # elif z == 5:
        #     np.append(low_alpha,az)

        # elif z == 6:
        #     np.append(high_alpha,az)

        # elif z == 7:
        #     np.append(low_beta,az)

        # elif z == 8:
        #     np.append(high_beta,az)

        # elif z == 9:
        #     np.append(low_gamma,az)

        # else:
        #     np.append(high_gamma,az)   
    #     z=+1
    # z=0

    
    

    