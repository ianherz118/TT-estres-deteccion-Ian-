#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:17:56 2021

@author: ianhj
"""
import numpy as np 
import pandas as pd

documento='/home/ianhj/Downloads/EEG_ian.xlsx'
df = pd.read_excel(documento)
print(df['EGG'])
separador = ","
separado = df.split(separador)
print(separado)
