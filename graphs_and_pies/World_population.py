
# coding: utf-8

# In[6]:

import pandas as pd
import numpy as np 
import pygal
from IPython.display import SVG
from pygal.style import *

health = pd.read_csv('data.csv')
health=health.drop(health.columns[[1,3,5]], axis=1)
health.columns = ['Country','Series','2015']
series = health['Series'].unique()

def new_df(n):
    newdf = health[(health['Series']==series[n])]
    newdf = newdf.drop(newdf.columns[1], axis=1)
    newdf.columns = ['Country',series[n]]
    newdf = newdf.replace('..', np.NaN)
    return newdf

h2,h3,h4,h5,h6,h7,h8,h9 = [new_df(number) for number in range(2,10)]

new = pd.merge(h2, h3, on='Country')
new = pd.merge(new, h4, on='Country')
new = pd.merge(new, h5, on='Country')
new = pd.merge(new, h6, on='Country')
new = pd.merge(new, h7, on='Country')
new = pd.merge(new, h8, on='Country')
new = pd.merge(new, h9, on='Country')
new = new.drop(new.index[[246,254,222,221,220,212,211,210,207,189,188,178,177,175,172,155,154,153,152,137,136,135,128,127,126,125,124,123,98,97,79,75,74,73,72,71,63,62,61,60,40,10]])
new['Country'][193]='Russia'
new = new.set_index('Country')


countries = []
for item in new.index.values:
     countries.append(item) 

#-----Total-Population--Ordinary--StackedBar-----
chart = pygal.StackedBar()
chart.title = series[7]
other_total = 0
for i in range(0, len(countries)):
            if float(new[series[7]][i])>100000000:
                chart.add(countries[i], float(new[series[7]][i]))
            elif float(new[series[7]][i])<100000000:
                other_total+=float(new[series[7]][i])
chart.add('Other countries', other_total)    
chart.render_to_file('population_total.svg')
SVG(filename='population_total.svg')    

#-----Rural-versus-Urban-------
def chart_stacked_ur(n,nn,k,name):
    chart = pygal.StackedBar()
    chart.title = 'Rural vs Urban'
    for i in range(0, len(countries)):
            if (float(new[series[n]][i])+float(new[series[nn]][i]))>k:
                chart.add(countries[i]+' Rural', float(new[series[n]][i]))
                chart.add(countries[i]+' Urban', float(new[series[nn]][i]))
    chart.render_to_file(name)
      
chart_stacked_ur(8,9,1000000000,'rural_vs_urban.svg')
SVG(filename='rural_vs_urban.svg')    

#-----Pie-Chart-Total-Population--
pie_chart = pygal.Pie(inner_radius=.35, style=DefaultStyle)
pie_chart.title = 'World population'
other_total = 0
for i in range(0, len(countries)):
                if float(new[series[7]][i])>100000000:
                    pie_chart.add(countries[i], float(new[series[7]][i]))
                elif float(new[series[7]][i])<100000000:
                    other_total+=float(new[series[7]][i])
pie_chart.add('Other countries', other_total)
pie_chart.render_to_file('population_pie.svg')    
SVG(filename='population_pie.svg')    

#-----Pie-Chart-Total-Population--with-urban-and-rural-divisions----
pie_chart = pygal.Pie(half_pie=True,style=CleanStyle)
pie_chart.title = 'World population'
other_total_urban=0
other_total_rural=0
new[series[8]] = new[series[8]].fillna(0)
new[series[9]] = new[series[9]].fillna(0)
for i in range(0, len(countries)):
                if float(new[series[7]][i])>100000000:
                    pie_chart.add(countries[i],[float(new[series[8]][i]),float(new[series[9]][i])])
                elif float(new[series[7]][i])<100000000:
                    other_total_urban+=float(new[series[9]][i])
                    other_total_rural+=float(new[series[8]][i])
                    
pie_chart.add('Other countries', [other_total_rural,other_total_urban])
pie_chart.render_to_file('population_pie_urban_rural.svg')    
SVG(filename='population_pie_urban_rural.svg')

