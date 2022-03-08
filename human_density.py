from gettext import install
from matplotlib import cm
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap
import matplotlib.pyplot as plt
import matplotlib.colors as colors


import rasterio
import numpy as np

#GETTING TIF IMAGE AND DEFINING IT
tif_file = rasterio.open('E:\\Program Files\\Faculdade\\2022\\Codes\\Human Density Map\\Population_density_with_python\\GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0_13_10.tif')
ghs_data = tif_file.read()

#THESE ATTRIBUTES GET THE GENERAL RASTER IMAGE GRAPHIC SIZE. PRINTING IT JUST TO KNOW IF THE IMAGE IS NOT TOO BIG FOR LOCAL COMPUTER PROCESSING
print("Tiff Boundary", tif_file.bounds)
print("Tiff CRS", tif_file.crs)
print("Data shape", ghs_data.shape)
print("Max value", np.amax(ghs_data)) #GET MAXIMUM VALUE OF PEOPLE PER KILOMETER SQUARE
print("Min value", np.amin(ghs_data)) #GET MINIMUM VALUE OF PEOPLE PER KILOMETER SQUARE, -200 EQUALS NULL VALUE

#
ghs_data[0][ghs_data[0] < 0.0] = 0.0

#PLOTTING
#THIS ONE PLOT THE MAP WITH A GRADIENT BASED ON THE MAXIMUM AND MINIMUN VALUES FOUND ON THE RASTER (-200 AND 32000 FOR THIS CASE)
ourcmap = cm.get_cmap('cool', 460)
newcolors = ourcmap(np.linspace(0, 1, 460))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors[:1, :] = background_colour
newcmp = ListedColormap(newcolors)

#fig, ax = plt.subplots(facecolor='#FCF6F5FF')
#fig.set_size_inches(14, 7)
#ax.imshow(ghs_data[0], norm=colors.LogNorm(), cmap=newcmp)
#ax.axis('off')
#plt.show()

#THIS IS AN ADAPTION WHERE THE BANDS OF COLOR ARE DEFINED IN THE CODE. IN THIS CASE I'VE USED 17 TONES OF THE GRADIENT TO PRINT THE MAP
our_cmap = cm.get_cmap('cool', 17)
newcolors = our_cmap(np.linspace(0, 1, 17))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors = np.vstack((background_colour, newcolors))
our_cmap = ListedColormap(newcolors)
bounds = [0.0, 1, 10, 20, 35, 75, 120, 300, 550, 1250, 3000, 5000, 7500, 10000, 12000, 17000, 21000, 32000, 50000]
norm = colors.BoundaryNorm(bounds, our_cmap.N)

fig, ax = plt.subplots(facecolor='#FCF6F5FF')
fig.set_size_inches(112, 56)
ax.imshow(ghs_data[0], norm=norm, cmap=our_cmap)
ax.axis('off')
plt.show()