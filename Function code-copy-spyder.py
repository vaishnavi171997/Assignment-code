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
    
#defining function for barchart and plotting the graph
def barchart(col_a,col_b,col_c,col_d,label_a,label_b,title,x_label,y_label):
    plt.figure(figsize=(10,10))
    plt.bar(matches[col_a],matches[col_b],width=0.4,label=label_a)
    plt.bar(matches[col_c],matches[col_d],width=0.3,label=label_b)
    plt.xlabel(x_label,fontsize=20)
    plt.ylabel(y_label,fontsize=20)
    plt.title(title,fontsize=20)
    plt.legend(prop={'size':16})
    plt.show()
    
#defining function for pie chart and plotting the graph 
def pie_chart(col_a,title,countries):
    plt.figure()
    #countries =['France','Germany','Spain','Norway']
    plt.pie(matches[col_a],labels=countries,autopct=('%0.1f%%'))
    plt.title(title)
    plt.legend(loc =2 ,bbox_to_anchor=(1,1.2))
    plt.show()
    
#defining function for histogram and plotting the graph 
def histogram(col_a,col_b,col_c,col_d,label_a,label_b,x_label,y_label,title):
    plt.figure(figsize=(25,8))
    plt.hist(matches[col_a],bins=20,label=label_a)
    plt.hist(matches[col_b],bins=20,label=label_b)
    plt.hist(matches[col_c],bins=5,label='prob1',rwidth=50)
    plt.hist(matches[col_d],bins=6,label='prob2',rwidth=50)
    plt.xlabel(x_label,fontsize=20)
    plt.ylabel(y_label,fontsize=20)
    plt.legend(prop={'size':16})
    plt.title(title,fontsize=20)
    plt.show()
    
#defining columns and reading the file
columns = ['score1','score2','prob1','prob2']
matches = pd.read_csv('C:\\Users\\HP\\Downloads\\applieddsassignment\\wwc_matches.csv',nrows=4,usecols=columns)

#calling the function for lineplot
lineplot('score1','score2','prob1','prob2','score1','score2','prob1','prob2')

#calling the function for barchart
barchart('score1','prob1','score2','prob2','score1','score2','Score of soccer teams','Scores','Probability')

#calling the function for pie_chart
pie_chart('score1','Scores of four countries',['France','Germany','Spain','Norway'])

#calling the function for histogram
histogram('score1','score2','prob1','prob2','score1','score2','Scores and Probability','Records','Histogram depicts Scores and Probability')
