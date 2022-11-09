# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:13:15 2022

@author: HP
"""

#Importing Pandas package to read the file 
import pandas as pd
#Importing matplotlib python package for data plotting and visualization
import matplotlib.pyplot as plt

#defining function for lineplot and plotting the graph
def lineplot(col_a,col_b,col_c,col_d,label_a,label_b,label_c,label_d):
    plt.figure()
    plt.plot(matches[col_a],linewidth=2,label=label_a)
    plt.plot(matches[col_b],linewidth=2,label=label_b)
    plt.plot(matches[col_c],linewidth=2,label=label_c)
    plt.plot(matches[col_d],linewidth=2,label=label_d)
    plt.xlabel('Game records',fontsize=15)
    plt.ylabel('Scores',fontsize=15)
    plt.title('Scores & Probablity of Team1 & Team2',fontsize=15)
    plt.legend(loc='upper center')
    plt.show()
    
    
#defining columns and reading the file
columns = ['score1','score2','prob1','prob2']
matches = pd.read_csv('C:\\Users\\HP\\Downloads\\applieddsassignment\\wwc_matches.csv',nrows=4,usecols=columns)

#calling the function for lineplot
lineplot('score1','score2','prob1','prob2','score1','score2','prob1','prob2')