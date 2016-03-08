
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt 
import matplotlib.image as mgimg
from matplotlib import animation
import matplotlib.image as image


fig, ax = plt.subplots(figsize=(16,12))
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

fig.patch.set_visible(False)
ax.axis('off')
# initiate an empty  list of "plotted" images 
myimages = []

#loops through available png:s
for p in range(0, 56):

    ## Read in picture
    fname = "/home/ketka/Git_projects/World_populaion_1960_2014_plotting_and_animation/map/population%03d.png" %p 
    img = image.imread(fname)
    
   
    imgplot = plt.imshow(img)
    
    # append AxesImage object to the list
    myimages.append([imgplot])

## create an instance of animation
my_anim = animation.ArtistAnimation(fig, myimages, interval=1500, blit=False, repeat=False)

## the 'save' method here belongs to the object you created above
my_anim.save("/home/ketka/Git_projects/World_populaion_1960_2014_plotting_and_animation/world_population_1960_2014.mp4")

## Showtime!

#plt.show()


