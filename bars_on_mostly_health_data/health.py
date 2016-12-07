
# coding: utf-8

# In[214]:

import pandas as pd
import numpy as np 
import pygal
from IPython.display import SVG
from pygal.style import *

health = pd.read_csv('data.csv')
health = health.drop(health.columns[[1,3,5]], axis=1)
health.columns = ['Country','Series','2015']
series = health['Series'].unique()

health2 = pd.read_csv('data_health.csv')
health2 = health2.drop(health2.columns[[1,3]], axis=1)
health2.columns = ['Series','Country','2015']
series2 = health2['Series'].unique()

def new_df(df,ss,n,nn):
    newdf = df[(df['Series']==ss[n])]
    newdf = newdf.drop(newdf.columns[nn], axis=1)
    newdf.columns = ['Country',ss[n]]
    newdf = newdf.replace('..', np.NaN)
    #newdf[series[n]] = newdf[series[n]].astype(float)
    return newdf

h2,h3,h4,h5,h6,h7 = [new_df(health,series,number,1) for number in range(2,8)]
hh0,hh1,hh2,hh3,hh4,hh5,hh6,hh7,hh8,hh9,hh10,hh11,hh12,hh13,hh14,hh15 = [new_df(health2,series2,number,0) for number in range(0,16)]


new = pd.merge(h2, h3, on='Country')
new = pd.merge(new, h7, on='Country')
new = pd.merge(new, hh0, on='Country')
new = pd.merge(new, hh5, on='Country')
new = pd.merge(new, hh8, on='Country')
new = pd.merge(new, hh9, on='Country')
new = pd.merge(new, hh10, on='Country')
new = pd.merge(new, hh13, on='Country')
new = new.drop(new.index[[246,254,222,221,220,212,211,210,207,189,188,178,177,175,172,155,154,153,152,137,136,135,128,127,126,125,124,123,98,97,79,75,74,73,72,71,63,62,61,60,40,10]])
new['Country'][193]='Russia'
new = new.set_index('Country')

countries = []
for item in new.index.values:
     countries.append(item) 


# #-----Mortal-kids-------------
# def chart_bar_simple_with_two(n,nn,k,kk,name):
#     chart = pygal.Bar(print_values=True, print_values_position='top',style=DefaultStyle(value_font_size=12))
#     chart.title = 'Dead kids(<5 years) for 1000'
#     for i in range(0, len(countries)):
#             if (float(new[series[n]][i])+float(new[series[nn]][i]))>k  or countries[i] in ['Ukraine','Canada', 'United States']:
#                 chart.add(countries[i], round(float(new[series[n]][i])+float(new[series[nn]][i])))
#             elif (float(new[series[n]][i])+float(new[series[nn]][i]))<kk:
#                 chart.add(countries[i], float(new[series[n]][i])+float(new[series[nn]][i]))    
#     chart.render_to_file(name)
      
# chart_bar_simple_with_two(2,3,170,5,'mortal_kids.svg')
# SVG(filename='mortal_kids.svg') 


# #-----People-with-HIV----------
def chart_bar_simple(n,k,kk,name,title):
    chart = pygal.Bar()
    chart.title = title
    new[series2[n]] = new[series2[n]].fillna(0)
    for i in range(0, len(countries)):
            if float(new[series2[n]][i])>=k  or countries[i] in ['Ukraine']:
                chart.add(countries[i], round(float(new[series2[n]][i])))
            elif float(new[series2[n]][i])<kk and float(new[series2[n]][i])!=0:
                chart.add(countries[i], float(new[series2[n]][i]))    
    chart.render_to_file(name)
      
chart_bar_simple(0,200000,0,'people_with_hiv.svg','People with HIV')
SVG(filename='people_with_hiv.svg') 

# #-----Percent-of-people-with-HIV------------
chart_bar_simple(5,15,0,'percent_of_people_with_diabetes.svg','Percent of people with Diabetes')
SVG(filename='percent_of_people_with_diabetes.svg') 

# #-----Percent-of-people-immunized-with-BCG------------
chart_bar_simple(8,99.9,70,'immunization_bcg_percent.svg','Immunization BCG, percent')
SVG(filename='immunization_bcg_percent.svg') 

# #-----Percent-of-people-immunized-with-DPT------------
chart_bar_simple(9,99.9,70,'immunization_dpt_percent.svg','Immunization DPT, percent')
SVG(filename='immunization_dpt_percent.svg') 

# #-----Percent-of-people-immunized-with-Pol3------------
chart_bar_simple(10,99.9,70,'immunization_pol3_percent.svg','Immunization Pol3, percent')
SVG(filename='immunization_pol3_percent.svg') 

# #-----Percent-of-literacy-adult-----------
chart_bar_simple(13,100,60,'literacy_rate_adult.svg','Literacy rate of adult people, percent')
SVG(filename='literacy_rate_adult.svg') 

# #-----Percent-of-people-with-HIV------------
def chart_bar_percent(n,nn,k,name,title):
    chart = pygal.Bar()
    chart.title = title
    new[series2[n]] = new[series2[n]].fillna(0)
    for i in range(0, len(countries)):
            if (float(new[series2[n]][i])/float(new[series[nn]][i])*100)>2  or countries[i] in ['Ukraine']:
                chart.add(countries[i], (float(new[series2[n]][i])/float(new[series[nn]][i])*100))
    chart.render_to_file(name)

chart_bar_percent(0,7,3,'percent_of_people_with_hiv.svg','Percent of people with HIV')
SVG(filename='percent_of_people_with_hiv.svg') 

