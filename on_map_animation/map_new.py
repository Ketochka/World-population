
# coding: utf-8

# In[4]:

import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.io.shapereader as shpreader
import csv

## specifying map view
fig, ax = plt.subplots(figsize=(20,12), 
                       subplot_kw={'projection': ccrs.PlateCarree()})
fig.subplots_adjust(left=0, bottom=-0.2, right=1, top=1,  wspace=None, hspace=None)


shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

## defining colors and population points where color is changed
colors = ['#fff5f0', '#fee0d2', '#fcbba1',
          '#fc9272', '#fb6a4a', '#ef3b2c',
          '#cb181d', '#a50f15', '#67000d', '#3d0007', '#330006', '#230004']
points = [5000000, 20000000, 50000000,
          100000000,500000000,750000000,
          870000000, 1000000000, 1100000000, 1250000000, 1350000000]

## a function for calling a detailed legend with all our colors and population numbers
def legend_details(y, label_sp):
               return mpatches.Patch(facecolor=colors[y], edgecolor='black', lw=0.2, label=label_sp)
sq_1 = legend_details(0, '< 5m')  
sq_2 = legend_details(1, '< 20m')
sq_3 = legend_details(2, '< 50m')  
sq_4 = legend_details(3, '< 100m')
sq_5 = legend_details(4, '< 500m')  
sq_6 = legend_details(5, '< 750m')
sq_7 = legend_details(6, '< 870m')  
sq_8 = legend_details(7, '< 1b')
sq_9 = legend_details(8, '< 1.1b')  
sq_10 = legend_details(9, '< 1.25b')
sq_11 = legend_details(10,'> 1.25b')    
sq_12 = legend_details(11,'> 1.35b') 

legend = plt.legend(handles=[sq_1, sq_2, sq_3, sq_4, sq_5, sq_6, sq_7, sq_8, sq_9, sq_10, sq_11, sq_12],ncol=1,
                loc='lower left', bbox_to_anchor=(0.045, 0.14), fancybox=True, fontsize=20)
legend.get_frame().set_edgecolor('#b8acad')    
for text in legend.get_texts():
        text.set_color('#474142')
               

## reading data from csv
#mpl.rc('font',family='Times New Roman')
population_by_country = '/home/ketka/Git_projects/World_populaion_1960_2014_plotting_and_animation/datasets/population_by_country_new.csv'

pp = []
years = []
for i in range(1960, 2015):
    years.append('Population by country\n'+str(i)+'\n')
    
pop_by_year = [[]]*len(years)   

countries_pop = []
country = []

## reading csv file - setting a link between population by country by a specific year
## function makes a picture of plotted poppulaion data of a specific year starting with 0=1960
def make_pic(x):
    l=x
    y=l+4
    with open(population_by_country) as ff:
            reader_ff = csv.reader(ff)
            for i in range(1,6):
                next(reader_ff)
            for row in reader_ff:
                countries_pop.append(str(row[0]))
                pop_by_year[l].append(int(row[y]))


    def define_color(x):
         ax.add_geometries(each.geometry, ccrs.PlateCarree(),
                facecolor = colors[x], edgecolor='#544749',
                label=countries_pop[i])

    pp = pop_by_year[l]        

    for each in countries:
        for i in range(0, len(countries_pop)):
             if each.attributes['name'] == countries_pop[i]:
                        if pp[i] <= points[0]:
                            define_color(0)
                        if pp[i] > points[0] and pp[i] <= points[1]:
                            define_color(1) 
                        if pp[i] > points[1] and pp[i] <= points[2]:
                            define_color(2) 
                        if pp[i] > points[2] and pp[i] <= points[3]:
                            define_color(3) 
                        if pp[i] > points[3] and pp[i] <= points[4]:
                            define_color(4) 
                        if pp[i] > points[4] and pp[i] <= points[5]:
                            define_color(5) 
                        if pp[i] > points[5] and pp[i] <= points[6]:
                            define_color(6) 
                        if pp[i] > points[6] and pp[i] <= points[7]:
                            define_color(7) 
                        if pp[i] > points[7] and pp[i] <= points[8]:
                            define_color(8) 
                        if pp[i] > points[8] and pp[i] <= points[9]:
                            define_color(10)    
                        if pp[i] > points[9] and pp[i] <= points[10]:
                            define_color(10)
                        if pp[i] > points[10]:
                            define_color(11)    


    ax.set_title(years[l],fontsize=40, color='#474142')
    ax.outline_patch.set_edgecolor('#ffffff')

    #plt.show()
    plt.savefig('/home/ketka/Git_projects/World_populaion_1960_2014_plotting_and_animation/map/population%03d' %l)
## calling the function to make a picture of a specific year
## (don't know why but it gives true data only when is called only by 1 year in a call)
## this: 
##      for i in range(0,55):
##            make_pic(i)  
## gives a list of the same pictures with plotted data of the first year
## setting any delays doesn't help as well
make_pic(5)

