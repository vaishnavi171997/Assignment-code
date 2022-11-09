# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:13:15 2022

@author: HP
"""

#Importing Pandas package to read the file 
import pandas as pd
#Importing matplotlib python package for data plotting and visualization
import matplotlib.pyplot as plt

#defining columns and reading the file
columns = ['score1','score2','prob1','prob2']
matches = pd.read_csv('C:\\Users\\HP\\Downloads\\applieddsassignment\\wwc_matches.csv',nrows=4,usecols=columns)